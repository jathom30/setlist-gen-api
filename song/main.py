from fastapi import FastAPI

from . import models
from .database import engine
from .routers import song, user, authentication

apiDescription = """
Auto-generate setlists

## Songs

View, update, add, and remove songs from your library

## Setlists

Auto-generate setlists based on preferred length and number of sets.
Reorder, replace, remove, or add songs to generate the perfect list.
"""

app = FastAPI(title="Setlist Generator API",
              description=apiDescription, version="0.1.0")

models.Base.metadata.create_all(engine)

app.include_router(song.router)
app.include_router(user.router)
app.include_router(authentication.router)
