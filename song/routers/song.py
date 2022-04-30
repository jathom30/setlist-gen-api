from fastapi import APIRouter, Depends, status
from typing import List
from sqlalchemy.orm import Session
from song import models
from song.database import get_db
from song.oauth2 import get_current_user
from song.schemas import ShowSong, ShowUser, Song, User
from ..repository import song

router = APIRouter(
    prefix="/songs",
    tags=["Songs"],
    dependencies=[Depends(get_current_user)]
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_song(request: Song, db: Session = Depends(get_db), user: Session = Depends(get_current_user)):
    return song.create(db, request, user)


@router.get('/', response_model=List[ShowSong])
def get_all_songs(db: Session = Depends(get_db), user: Session = Depends(get_current_user)):
    return song.get_all(db, user)


@router.get('/{id}', response_model=ShowSong)
def get_song(id, db: Session = Depends(get_db), user: Session = Depends(get_current_user)):
    return song.get(id, db, user)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_song(id, db: Session = Depends(get_db), user: Session = Depends(get_current_user)):
    return song.destroy(db, id, user)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_song(id, request: Song, db: Session = Depends(get_db), user: Session = Depends(get_current_user)):
    return song.update(id, request, db, user)
