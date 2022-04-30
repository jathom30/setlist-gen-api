from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from song.schemas import Parent
from .. import models


def get_user_parent_lists(db: Session, user: models.Parent):
    userId = user.id
    if not userId:
        return []
    return db.query(models.Parent).filter(models.Parent.user_id == userId)


def get_all(db: Session, user: models.User):
    return get_user_parent_lists(db, user).all()


def get(id: int, db: Session, user: models.User):
    parent = get_user_parent_lists(db, user).first()
    if not parent:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Parent list not found")
    return parent


def create(db: Session, request: Parent, user: models.User):
    new_parent = models.Parent(
        name=request.name,
        setlist_ids=request.setlist_ids,
        user_id=user.id,
    )
    db.add(new_parent)
    db.commit()
    db.refresh(new_parent)
    return new_parent


def destroy(db: Session, id: int, user: models.User):
    parent = get_user_parent_lists(db, user).filter(models.Parent.id == id)
    if not parent.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Parent list not found")

    parent.delete(synchronize_session=False)
    db.commit()
    return 'deleted'


def update(id: int, request: Parent, db: Session, user: models.User):
    parent = get_user_parent_lists(db, user).filter(models.Parent.id == id)
    if not parent.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Parent list not found")
    parent.update({
        models.Parent.name: request.name,
        models.Parent.setlist_ids: request.setlist_ids,
    }, synchronize_session=False)
    db.commit()
    return request
