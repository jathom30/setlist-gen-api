from pydantic import BaseModel
from typing import Optional, List
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
    key: Optional[str] = None
    notes: Optional[str] = None


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str

    class Config():
        orm_mode = True


class ShowSong(BaseModel):
    id: int
    name: str
    tempo: Tempo
    feel: Feel
    placement: SongPlacement
    length: int
    is_cover: Optional[bool] = False
    exclude: Optional[bool] = False
    key: Optional[str] = None
    notes: Optional[str] = None
    # user: ShowUser

    class Config():
        orm_mode = True


class Setlist(BaseModel):
    name: str
    song_ids: List[int]


class ShowSetlist(BaseModel):
    id: int
    name: str
    song_ids: List[str]

    class Config():
        orm_mode = True


class Parent(BaseModel):
    name: str
    setlist_ids: List[int]


class ShowParent(Parent):
    id: int

    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class TokenData(BaseModel):
    email: Optional[str] = None
