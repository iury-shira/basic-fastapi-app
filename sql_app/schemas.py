from pydantic import BaseModel
from typing import List, Optional


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


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
