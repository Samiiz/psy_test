from fastapi import HTTPException
from schemas.users import CreateUser, User
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

def create_user(db: Session, user: CreateUser):
    user_data = user.dict()

    sql = text("INSERT INTO users (name, age, gender) VALUES (:name, :age, :gender) RETURNING id")
    result = db.execute(sql, params=user_data)
    db.commit()

    new_user_id = result.fetchone()[0]

    if new_user_id is None:
        raise HTTPException(status_code=400, detail="Could not find user_id")

    user_query = text("SELECT * FROM users WHERE id = :new_user_id")
    user_result = db.execute(user_query, {"new_user_id": new_user_id}).fetchone()

    if user_result is None:
        raise HTTPException(status_code=404, detail="Could not find user")

    return User.from_orm(user_result)