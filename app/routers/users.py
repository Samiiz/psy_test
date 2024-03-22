from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Union
import crud.sql as sql, schemas.users as users, database

router = APIRouter()

@router.post('/', response_model=users.User)
def create_user(user: users.CreateUser, db: Session = Depends(database.get_db)):
    db_user = sql.create_user(db, user)
    return db_user