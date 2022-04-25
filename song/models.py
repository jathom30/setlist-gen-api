from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Enum
from sqlalchemy.orm import relationship
from song.schemas import Feel, SongPlacement, Tempo
from .database import Base


class Song(Base):
    __tablename__ = 'songs'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    tempo = Column(Enum(Tempo))
    feel = Column(Enum(Feel))
    placement = Column(Enum(SongPlacement))
    length = Column(Integer)
    is_cover = Column(Boolean)
    exclude = Column(Boolean)
    key = Column(String)
    notes = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="songs")


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    songs = relationship('Song', back_populates="user")
