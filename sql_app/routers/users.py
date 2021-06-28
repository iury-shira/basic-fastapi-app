from typing import List
from .. import schemas, database, oauth2
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..repository import users as users_repository

router = APIRouter(
    prefix='/user',
    tags=['Users']
)

get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowUser])
def get_users(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return users_repository.get_all(db)


@router.get('/{id}', response_model=schemas.ShowUserWithMessages)
def get_user_by_id(id: int, db: Session = Depends(get_db),
                   current_user: schemas.User = Depends(oauth2.get_current_user)):
    return users_repository.get_by_id(id, db)


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db),
                current_user: schemas.User = Depends(oauth2.get_current_user)):
    return users_repository.create(request, db)
