from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from song.hashing import Hash

from song.schemas import Song, User
from .. import models


def create(request: User, db: Session):
    new_user = models.User(
        name=request.name,
        email=request.email,
        password=Hash.bcrypt(request.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user
