from pydantic import BaseModel
from typing import List, Optional
from.answers import UserAnswer
from datetime import datetime

class UserBase(BaseModel):
    name : str

class User(UserBase):
    id : int
    age : int
    gender : str
    created_at : datetime
    updated_at : datetime

    answers: Optional[List[UserAnswer]] = []

    class Config:
        from_attributes=True

class CreateUser(UserBase):
    age : int
    gender : str

class UpdateUser(UserBase):
    name  : str | None = None
    age : int | None = None
    gender : str | None = None