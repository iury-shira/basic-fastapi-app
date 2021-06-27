from typing import List
from .. import schemas, database, models
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()

get_db = database.get_db


@router.get('/message', response_model=List[schemas.ShowMessage], tags=['messages'])
def get_message(db: Session = Depends(get_db)):
    return db.query(models.Message).all()


@router.get('/message/{id}', response_model=schemas.ShowMessage, tags=['messages'])
def get_message_by_id(id: int, db: Session = Depends(get_db)):
    message = db.query(models.Message).filter(models.Message.id == id).first()

    if not message:
        message = {"detail": f"Message with id {id} not available"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)

    return message


@router.post('/message', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowMessage, tags=['messages'])
def create_message(request: schemas.Message, db: Session = Depends(get_db)):
    new_message = models.Message(title=request.title, body=request.body, user_id=1)     # TODO: change this hardcoded id
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    return new_message


@router.put('/message/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=schemas.ShowMessage, tags=['messages'])
def update_message(id: int, request: schemas.Message, db: Session = Depends(get_db)):
    message = db.query(models.Message).filter(models.Message.id == id)

    if not message.first():
        message = {"detail": f"Message with id {id} not available"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)

    message.update(request.dict())
    db.commit()
    return message.first()


@router.delete('/message/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['messages'])
def delete_message(id: int, db: Session = Depends(get_db)):
    message = db.query(models.Message).filter(models.Message.id == id)

    if not message.first():
        message = {"detail": f"Message with id {id} not available"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)

    message.delete(synchronize_session=False)
    db.commit()
    return
