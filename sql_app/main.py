from fastapi import FastAPI, Depends
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/message')
def create(request: schemas.Message, db: Session = Depends(get_db)):
    new_message = models.Message(title=request.title, body=request.body)
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    return new_message


@app.get('/message')
def get_messages(db: Session = Depends(get_db)):
    return db.query(models.Message).all()


@app.get('/message/{id}')
def get_messages_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(models.Message).filter(models.Message.id == id).first()
