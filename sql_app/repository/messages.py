from sqlalchemy.orm import Session
from .. import schemas, models
from fastapi import status, HTTPException


def get_all(db: Session):
    return db.query(models.Message).all()


def get_by_id(id: int, db: Session):
    message = db.query(models.Message).filter(models.Message.id == id).first()

    if not message:
        message = {"detail": f"Message with id {id} not available"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)

    return message


def create(request: schemas.Message, db: Session):
    new_message = models.Message(title=request.title, body=request.body, user_id=1)  # TODO: change this hardcoded id
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    return new_message


def update(id: int, request: schemas.Message, db: Session):
    message = db.query(models.Message).filter(models.Message.id == id)

    if not message.first():
        message = {"detail": f"Message with id {id} not available"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)

    message.update(request.dict())
    db.commit()
    return message.first()


def delete(id: int, db: Session):
    message = db.query(models.Message).filter(models.Message.id == id)

    if not message.first():
        message = {"detail": f"Message with id {id} not available"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)

    message.delete(synchronize_session=False)
    db.commit()
    return
