from typing import List
from fastapi import APIRouter, Depends, status
from song.database import get_db
from song.oauth2 import get_current_user
from sqlalchemy.orm import Session
from song.schemas import Parent, ShowParent
from song.repository import parent

router = APIRouter(
    prefix='/parent-list',
    tags=["Parent List"],
    dependencies=[Depends(get_current_user)]
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_parent(request: Parent, db: Session = Depends(get_db), user: Session = Depends(get_current_user)):
    return parent.create(db, request, user)


@router.get('/', response_model=List[ShowParent])
def get_all_parent_lists(db: Session = Depends(get_db), user: Session = Depends(get_current_user)):
    return parent.get_all(db, user)


@router.get('/{id}', response_model=ShowParent)
def get_parent_lists(id: int, db: Session = Depends(get_db), user: Session = Depends(get_current_user)):
    return parent.get(id, db, user)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_parent_list(id, db: Session = Depends(get_db), user: Session = Depends(get_current_user)):
    return parent.destroy(db, id, user)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_parent_list(id, request: Parent, db: Session = Depends(get_db), user: Session = Depends(get_current_user)):
    return parent.update(id, request, db, user)
