from pydantic import BaseModel
from typing import List, Optional

class StaffBase(BaseModel):
    nickname : str

class Staff(StaffBase):
    id : int

    class Config:
        from_attributes=True

class CreateStaff(StaffBase):
    nickname : str
    password : str

class UpdateStaff(StaffBase):
    nickname : str | None = None
    password : str | None = None

class DeleteStaff(StaffBase):
    password : str