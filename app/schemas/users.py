from pydantic import BaseModel
from typing import List, Optional
from.answers import Answer

class UserBase(BaseModel):
    name : str

class User(UserBase):
    id : int
    age : int
    gender : str

    answers: Optional[List[Answer]] = []

    class Config:
        from_attributes=True

class CreateUser(UserBase):
    age : int
    gender : str

class UpdateUser(UserBase):
    name  : str | None = None
    age : int | None = None
    gender : str | None = None