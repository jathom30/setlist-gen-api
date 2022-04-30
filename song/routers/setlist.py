from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from song.database import get_db
from song.oauth2 import get_current_user
from song.schemas import Setlist, ShowSetlist
from song.repository import setlist

router = APIRouter(
    prefix="/setlists",
    tags=["Setlists"],
    dependencies=[Depends(get_current_user)]
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_setlist(request: Setlist, db: Session = Depends(get_db), user: Session = Depends(get_current_user)):
    return setlist.create(db, request, user)


@router.get('/', response_model=List[ShowSetlist])
def get_all_setlists(db: Session = Depends(get_db), user: Session = Depends(get_current_user)):
    return setlist.get_all(db, user)


@router.get('/{id}', response_model=ShowSetlist)
def get_setlist(id, db: Session = Depends(get_db), user: Session = Depends(get_current_user)):
    return setlist.get(id, db, user)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_setlist(id, db: Session = Depends(get_db), user: Session = Depends(get_current_user)):
    return setlist.destroy(db, id, user)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_setlist(id, request: Setlist, db: Session = Depends(get_db), user: Session = Depends(get_current_user)):
    return setlist.update(id, request, db, user)
