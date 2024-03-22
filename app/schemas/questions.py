from pydantic import BaseModel
from typing import List, Optional

class QuestionBase(BaseModel):
    question : str

class Question(QuestionBase):
    id : int

    class Config:
        from_attributes=True

class CreateQuestion(QuestionBase):
    id : int

class UpdateQuestion(QuestionBase):
    question : str | None = None