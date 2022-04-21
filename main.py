from contextlib import nullcontext
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
from enum import Enum

app = FastAPI()


class Tempo(Enum):
    BALLAD = 'ballad'
    CHILL = 'chill'
    MEDIUM = 'medium'
    UP = 'up'
    BURNER = 'burner'


class Feel(Enum):
    COUNTRY = 'country'
    LATIN = 'latin'
    SWING = 'swing'
    BLUES = 'blues'
    ROCK = 'rock'
    FUNK = 'funk'
    OTHER = 'other'


class SongPlacement(Enum):
    OPENER = 'opener'
    CLOSER = 'closer'
    OTHER = 'other'


class Song(BaseModel):
    name: str
    tempo: Tempo
    feel: List[Feel]
    placement: SongPlacement
    length: int
    isCover: Optional[bool] = False
    exclude: Optional[bool] = False
    key: Optional[str] = nullcontext
    notes: Optional[str] = nullcontext


@app.get('/songs')
def get_songs():
    return {'data': 'song list'}


@app.get('/songs/{id}')
def get_song(id: str):
    return {'data': id}


@app.post('/songs')
def post_song(request: Song):
    return request


@app.delete('/songs/{id}')
def delete_song(id: str):
    return {'data': id}
