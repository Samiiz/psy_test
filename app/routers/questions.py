from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Union, List
from crud import sql
from schemas import questions
import database

router = APIRouter()

@router.post('/', response_model=questions.Question)
def create_question(question: str, db: Session = Depends(database.get_db)):
    return sql.create_question(db, question)

@router.get('/{question_id}', response_model=questions.Question)
def get_question(question_id: int, db: Session = Depends(database.get_db)):
    question_id = int(question_id)

    if isinstance(question_id, int):
        return sql.get_question_id(db, question_id)
    else:
        raise HTTPException(status_code=404, detail="Question Not Found")

@router.get('/', response_model=List[questions.Question])
def get_questions(skip: int, limit: int=10, db: Session = Depends(database.get_db)):
    return sql.get_questions(db, skip, limit)

@router.put('/{question_id}', response_model=questions.Question)
def update_question(question_id: int, question: questions.UpdateQuestion, db: Session = Depends(database.get_db)):
    return sql.update_question(db, question_id, question)

@router.delete('/{question_id}', response_model=questions.Question)
def delete_question(question_id: int, db: Session = Depends(database.get_db)):
    return sql.delete_question(db, question_id)