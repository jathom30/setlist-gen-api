from pydantic import BaseModel
from typing import Optional
from enum import Enum


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
    feel: Feel
    placement: SongPlacement
    length: int
    is_cover: Optional[bool] = False
    exclude: Optional[bool] = False
    key: Optional[str] = ''
    notes: Optional[str] = ''
    user_id: str


# remove user_id from response
class ShowSong(BaseModel):
    name: str
    tempo: Tempo
    feel: Feel
    placement: SongPlacement
    length: int
    is_cover: Optional[bool] = False
    exclude: Optional[bool] = False
    key: Optional[str] = ''
    notes: Optional[str] = ''

    class Config():
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str
