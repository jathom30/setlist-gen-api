import email
from typing import List
from fastapi import Depends, FastAPI, status, HTTPException
from .schemas import ShowSong, Song, User
from . import models
from .database import SessionLocal, engine
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/song', status_code=status.HTTP_201_CREATED)
def create_song(request: Song, db: Session = Depends(get_db)):
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
        user_id=request.user_id,
    )
    db.add(new_song)
    db.commit()
    db.refresh(new_song)
    return new_song


@app.get('/songs', response_model=List[ShowSong])
def get_all_songs(db: Session = Depends(get_db)):
    return db.query(models.Song).all()


@app.get('/songs/{id}', response_model=ShowSong)
def get_song(id, db: Session = Depends(get_db)):
    song = db.query(models.Song).filter(models.Song.id == id).first()
    if not song:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Song not found")
    return song


@app.delete('/song/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_song(id, db: Session = Depends(get_db)):
    song = db.query(models.Song).filter(models.Song.id == id)
    if not song.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Song not found")

    song.delete(synchronize_session=False)
    db.commit()
    return 'deleted'


@app.put('/songs/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_song(id, request: Song, db: Session = Depends(get_db)):
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
        models.Song.user_id: request.user_id,
    }, synchronize_session=False)
    db.commit()
    return request


@app.post('/user')
def create_user(request: User, db: Session = Depends(get_db)):
    new_user = models.User(
        name=request.name,
        email=request.email,
        password=request.password,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
