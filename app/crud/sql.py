from fastapi import HTTPException
from sqlalchemy import select, insert, update, delete
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from models import User as UserModel, Answer as AnswerModel
from schemas.users import CreateUser, User, UpdateUser
from schemas.answers import Answer
# from schemas.users import CreateUser, User
# from sqlalchemy.sql import text

# sqlalchemy core의 기능을 이용한 가동성 좋은 동기식 CRUD

def create_user(db: Session, user: CreateUser) -> User:
    sql = insert(UserModel).values(name=user.name, age=user.age, gender=user.gender).returning(UserModel.id)
    result = db.execute(sql)
    db.commit()
    new_user_id = result.fetchone().id

    if new_user_id is None:
        raise HTTPException(status_code=400, detail="User Not Created")
    try:
        new_user = db.query(UserModel).filter(UserModel.id == new_user_id).one()
    except NoResultFound:
        raise HTTPException(status_code=404, detail="User Not Found")

    return User.from_orm(new_user)

def get_user_id(db: Session, user_id: int) -> User:
    sql = select(UserModel).where(UserModel.id == user_id)
    try:
        result = db.execute(sql).scalar_one()
    except NoResultFound:
        raise HTTPException(status_code=404, detail="User not found")

    return User.from_orm(result)

def get_users(db: Session, skip: int = 0, limit: int = 10) -> list[User]:
    sql = select(UserModel).offset(skip).limit(limit)
    results = db.execute(sql).scalars().all()

    users = []
    for user in results:
        user_data = User.from_orm(user)
        answer_sql = select(AnswerModel).where(AnswerModel.user_id == user.id)
        answer_results = db.execute(answer_sql).scalars().all()
        user_data.answers = [Answer.from_orm(answer) for answer in answer_results]
        users.append(user_data)

    return users

def update_user(db: Session,  user_id: int, update_user: UpdateUser) -> User:
    user_data = update_user.dict()
    sql = update(UserModel).where(UserModel.id == user_id).values(**user_data)
    db.execute(sql)
    db.commit()

    user = get_user_id(db, user_id)
    
    return user

def delete_user(db: Session,  user_id: int) -> User:
    user = get_user_id(db, user_id)

    sql = (
        delete(UserModel).
        where(UserModel.id == user_id)
    )
    db.execute(sql)
    db.commit()

    return user


# 수동쿼리 버전
# def create_user(db: Session, user: CreateUser):
#     user_data = user.dict()

#     sql = text("INSERT INTO users (name, age, gender) VALUES (:name, :age, :gender) RETURNING id")
#     result = db.execute(sql, params=user_data)
#     db.commit()

#     new_user_id = result.fetchone()[0]

#     if new_user_id is None:
#         raise HTTPException(status_code=400, detail="Could not find user_id")

#     user_query = text("SELECT * FROM users WHERE id = :new_user_id")
#     user_result = db.execute(user_query, {"new_user_id": new_user_id}).fetchone()

#     if user_result is None:
#         raise HTTPException(status_code=404, detail="Could not find user")

#     return User.from_orm(user_result)

# def get_user_id(db: Session, user_id: int):
#     sql = text("SELECT * FROM users WHERE id = :user_id")
#     result = db.execute(sql, {"user_id": user_id}).fetchone()
#     return User.from_orm(result)

# def get_users(db: Session, skip: int = 0, limit: int = 10):
#     sql = text("SELECT * FROM users LIMIT :limit OFFSET :skip")
#     result = db.execute(sql, {"limit": limit, "skip": skip}).fetchall()
#     users = [User.from_orm(user) for user in result]

#     for user in users:
#         answer_sql = text("SELECT * FROM answers WHERE user_id = :user_id")
#         answer_results = db.execute(answer_sql, {"user_id": user['id']}).fetchall()
#         user['answers'] = [answer._asdict() for answer in answer_results]

#     return users

