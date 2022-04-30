from curses.ascii import HT
from typing import List
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from song.schemas import Setlist
from .. import models
from . import song


def get_user_setlists(db: Session, user: models.User):
    userId = user.id
    if not userId:
        return []
    setlists = db.query(models.Setlist).filter(
        models.Setlist.user_id == userId)
    return setlists


def create(db: Session, request: Setlist, user: models.User):
    new_setlist = models.Setlist(
        name=request.name,
        song_ids=request.song_ids,
        user_id=user.id,
    )
    db.add(new_setlist)
    db.commit()
    db.refresh(new_setlist)
    return new_setlist


def get_all(db: Session, user: models.User):
    return get_user_setlists(db, user).all()


def get(id: int, db: Session, user: models.User):
    setlist: Setlist = db.query(models.Setlist).filter(
        models.Setlist.id == id).first()
    if not setlist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Setlist not found"
        )
    return setlist


def destroy(db: Session, id: int, user: models.User):
    setlist = get_user_setlists(db, user).filter(models.Setlist.id == id)
    if not setlist.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Setlist not found")

    setlist.delete(synchronize_session=False)
    db.commit()
    return 'deleted'


def update(id: int, request: Setlist, db: Session, user: models.User):
    setlist = get_user_setlists(db, user).filter(models.Setlist.id == id)
    if not setlist.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Setlist not found")
    setlist.update({
        models.Setlist.name: request.name,
        models.Setlist.song_ids: request.song_ids,
    }, synchronize_session=False)
    db.commit()
    return request
