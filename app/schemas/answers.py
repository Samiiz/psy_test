from pydantic import BaseModel
from typing import List, Optional

class AnswerBase(BaseModel):
    user_id = int
    question_id = int

class Answer(AnswerBase):
    answer : str

    class Config:
        from_attributes=True