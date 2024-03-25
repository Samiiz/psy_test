from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Union, List
from crud import sql
from schemas import answers, users
import database

router = APIRouter()

@router.post('/', response_model=answers.Answer)
def create_answer(answer: answers.CreateAnswer, db: Session = Depends(database.get_db)):
    return sql.create_answer(db, answer)

@router.get('/{question_id}/', response_model=list[answers.QuestionAnswer])
def get_answers(question_id: int, skip: int, limit: int=10, db: Session = Depends(database.get_db)):

    try:
        return sql.get_answers(db, question_id, skip=skip, limit=limit)
    except:
        raise HTTPException(status_code=404, detail="Question Not Found")