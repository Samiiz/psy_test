from fastapi import APIRouter, Depends, HTTPException, FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from typing import Union, List
from crud import sql
from schemas.users import CreateUser
from schemas.answers import Answer, CreateAnswer
from models import User as UserModel, Question as QuestionModel, Answer as AnswerModel, Staff as StaffModel
import database

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/create_user", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("create_user.html", {"request": request})

@router.post("/create_user", response_class=HTMLResponse)
async def create_user(request: Request, user: CreateUser, db: Session = Depends(database.get_db)):
    try:
        user = sql.create_user(db, user)
    except HTTPException as e:
        return e
    return RedirectResponse("/create_user", status_code=303)

@router.get("/test/{user_id}", response_class=HTMLResponse)
async def quiz(request: Request, user_id: int, db: Session = Depends(database.get_db)):
    try:
        user = sql.get_user_id(db, user_id)
        questions = sql.get_questions(db)
    except HTTPException as e:
        return e
    return templates.TemplateResponse("quiz.html", {"request": request, "user": user, "questions": questions})

@router.post("/submit_answers", response_class=HTMLResponse)
async def submit_answers(request: Request, user_id: int, answers: List[CreateAnswer], db: Session = Depends(database.get_db)):
    try:
        for ans in answers:
            sql.create_answer(db, ans)
    except HTTPException as e:
        return e
    return RedirectResponse("/", status_code=303)