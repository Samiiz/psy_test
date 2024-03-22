from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Union, List
import crud.sql as sql, schemas.users as users, database

router = APIRouter()

@router.post('/', response_model=users.User)
def create_user(user: users.CreateUser, db: Session = Depends(database.get_db)):
    return sql.create_user(db, user)

@router.get('/{user_id}', response_model=users.User)
def get_user(user_id: int, db: Session = Depends(database.get_db)):
    user_id = int(user_id)

    if isinstance(user_id, int):
        return sql.get_user_id(db, user_id)

@router.get('/', response_model=List[users.User])
def get_users(skip: int, limit: int=10, db: Session = Depends(database.get_db)):
    return sql.get_users(db, skip, limit)

@router.put('/{user_id}', response_model=users.User)
def update_user(user_id: int, user: users.UpdateUser, db: Session = Depends(database.get_db)):
    return sql.update_user(db, user_id, user)

@router.delete('/{user_id}', response_model=users.User)
def delete_user(user_id: int, db: Session = Depends(database.get_db)):
    db_user = sql.delete_user(db, user_id)

    if db_user is None:
        raise HTTPException(status_code=404, detail="User Not Found")
    
    return db_user