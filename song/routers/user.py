from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from song.database import get_db
from song.schemas import ShowUser, User
from ..repository import user

router = APIRouter(
    prefix="/user",
    tags=["Users"],
)


@router.post('/', response_model=ShowUser)
def create_user(request: User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get('/{id}', response_model=ShowUser)
def get_users(id, db: Session = Depends(get_db)):
    return user.get(id, db)
