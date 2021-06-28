from typing import List
from sqlalchemy.orm import Session
from .. import schemas, models
from fastapi import status, HTTPException
from ..hashing import Hash


def get_all(db: Session):
    return db.query(models.User).all()


def get_by_id(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        message = {"detail": f"Message with id {id} not available"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)

    return user


def create(request: schemas.User, db: Session):
    hashed_pwd = Hash.bcrytp(request.password)
    new_user = models.User(name=request.name, email=request.email, password=hashed_pwd)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
