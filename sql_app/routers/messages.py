from typing import List
from .. import schemas, database, oauth2
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..repository import messages as messages_repository

router = APIRouter(
    prefix='/message',
    tags=['Messages']
)

get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowMessage])
def get_messages(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return messages_repository.get_all(db)


@router.get('/{id}', response_model=schemas.ShowMessage)
def get_message_by_id(id: int, db: Session = Depends(get_db),
                      current_user: schemas.User = Depends(oauth2.get_current_user)):
    return messages_repository.get_by_id(id, db)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowMessage)
def create_message(request: schemas.Message, db: Session = Depends(get_db),
                   current_user: schemas.TokenData = Depends(oauth2.get_current_user)):
    return messages_repository.create(request, db, current_user)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=schemas.ShowMessage)
def update_message(id: int, request: schemas.Message, db: Session = Depends(get_db),
                   current_user: schemas.TokenData = Depends(oauth2.get_current_user)):
    return messages_repository.update(id, request, db, current_user)


@router.delete('/{id}', status_code=status.HTTP_202_ACCEPTED)
def delete_message(id: int, db: Session = Depends(get_db),
                   current_user: schemas.TokenData = Depends(oauth2.get_current_user)):
    messages_repository.delete(id, db, current_user)
    return
