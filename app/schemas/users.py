from pydantic import BaseModel
from typing import List, Optional

class UserBase(BaseModel):
    name : str

class User(UserBase):
    id : int
    age : int
    gender : str

    class Config:
        from_attributes=True

class CreateUser(UserBase):
    age : int
    gender : str