from pydantic import BaseModel
from typing import List


class Message(BaseModel):
    title: str
    body: str

    class Config:
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True


class ShowUserWithMessages(ShowUser):
    messages: List[Message] = []


class ShowMessage(Message):
    user: ShowUser
