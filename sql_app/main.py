from fastapi import FastAPI, Depends, Response, status, HTTPException
from . import schemas, models
from .database import engine, SessionLocal
from .hashing import Hash
from sqlalchemy.orm import Session
from typing import List


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/message', response_model=List[schemas.ShowMessage], tags=['messages'])
def get_message(db: Session = Depends(get_db)):
    return db.query(models.Message).all()


@app.get('/message/{id}', response_model=schemas.ShowMessage, tags=['messages'])
def get_message_by_id(id: int, db: Session = Depends(get_db)):
    message = db.query(models.Message).filter(models.Message.id == id).first()

    if not message:
        message = {"detail": f"Message with id {id} not available"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)

    return message


@app.post('/message', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowMessage, tags=['messages'])
def create_message(request: schemas.Message, db: Session = Depends(get_db)):
    new_message = models.Message(title=request.title, body=request.body, user_id=1)     # TODO: change this hardcoded id
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    return new_message


@app.put('/message/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=schemas.ShowMessage, tags=['messages'])
def update_message(id: int, request: schemas.Message, db: Session = Depends(get_db)):
    message = db.query(models.Message).filter(models.Message.id == id)

    if not message.first():
        message = {"detail": f"Message with id {id} not available"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)

    message.update(request.dict())
    db.commit()
    return message.first()


@app.delete('/message/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['messages'])
def delete_message(id: int, db: Session = Depends(get_db)):
    message = db.query(models.Message).filter(models.Message.id == id)

    if not message.first():
        message = {"detail": f"Message with id {id} not available"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)

    message.delete(synchronize_session=False)
    db.commit()
    return


@app.get('/user/{id}', response_model=schemas.ShowUser, tags=['users'])
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        message = {"detail": f"Message with id {id} not available"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)

    return user


@app.post('/user', response_model=schemas.ShowUser, tags=['users'])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    hashed_pwd = Hash.bcrytp(request.password)
    new_user = models.User(name=request.name, email=request.email, password=hashed_pwd)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
