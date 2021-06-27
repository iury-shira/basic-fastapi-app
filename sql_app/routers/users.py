from .. import schemas, database
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..repository import users as users_repository

router = APIRouter(
    prefix='/user',
    tags=['Users']
)

get_db = database.get_db


@router.get('/{id}', response_model=schemas.ShowUserWithMessages)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    return users_repository.get_by_id(id, db)


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return users_repository.create(request, db)
