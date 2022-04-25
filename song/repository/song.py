from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from song.schemas import Song, User
from .. import models


def get_all(db: Session):
    songs = db.query(models.Song).all()
    return songs


def get(id: int, db: Session):
    song = db.query(models.Song).filter(models.Song.id == id).first()
    if not song:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Song not found")
    return song


def create(db: Session, request: User):
    new_song = models.Song(
        name=request.name,
        tempo=request.tempo,
        feel=request.feel,
        placement=request.placement,
        length=request.length,
        is_cover=request.is_cover,
        exclude=request.exclude,
        key=request.key,
        notes=request.notes,
        user_id=1,
    )
    db.add(new_song)
    db.commit()
    db.refresh(new_song)
    return new_song


def destroy(db: Session, id: int):
    song = db.query(models.Song).filter(models.Song.id == id)
    if not song.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Song not found")

    song.delete(synchronize_session=False)
    db.commit()
    return 'deleted'


def update(id: int, request: Song, db: Session):
    song = db.query(models.Song).filter(models.Song.id == id)
    if not song.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Song not found")
    song.update({
        models.Song.name: request.name,
        models.Song.tempo: request.tempo,
        models.Song.feel: request.feel,
        models.Song.placement: request.placement,
        models.Song.length: request.length,
        models.Song.is_cover: request.is_cover,
        models.Song.exclude: request.exclude,
        models.Song.key: request.key,
        models.Song.notes: request.notes,
    }, synchronize_session=False)
    db.commit()
    return request
