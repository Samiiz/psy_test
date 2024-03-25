from pydantic import BaseModel
from typing import List, Optional

class AnswerBase(BaseModel):
    user_id : int
    question_id : int

class Answer(AnswerBase):
    id : int
    answer : bool

    class Config:
        from_attributes=True


class CreateAnswer(AnswerBase):
    answer: bool


class UserAnswer(BaseModel):
    question_id : int
    answer : bool

    class Config:
        from_attributes=True

class QuestionAnswer(BaseModel):
    user_id : int
    answer : bool

    class Config:
        from_attributes=True
