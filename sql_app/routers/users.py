from typing import List
from .. import schemas, database, models
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from ..hashing import Hash

router = APIRouter()

get_db = database.get_db


@router.get('/user/{id}', response_model=schemas.ShowUserWithMessages, tags=['users'])
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        message = {"detail": f"Message with id {id} not available"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)

    return user


@router.post('/user', response_model=schemas.ShowUser, tags=['users'])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    hashed_pwd = Hash.bcrytp(request.password)
    new_user = models.User(name=request.name, email=request.email, password=hashed_pwd)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
