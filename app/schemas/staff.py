from pydantic import BaseModel
from typing import List, Optional

class StaffBase(BaseModel):
    nickname : str

class CreateStaff(StaffBase):
    id : str
    password : str

class UpdateStaff(StaffBase):
    nickname : str | None = None
    password : str | None = None