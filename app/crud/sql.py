from fastapi import HTTPException
from sqlalchemy import select, insert, update, delete
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from models import User as UserModel, Answer as AnswerModel, Question as QuestionModel, Staff as StaffModel
from schemas.users import CreateUser, User, UpdateUser
from schemas.answers import Answer, CreateAnswer, QuestionAnswer
from schemas.questions import Question, CreateQuestion, UpdateQuestion
from schemas.staff import Staff, CreateStaff, UpdateStaff, DeleteStaff
from typing import List
# from schemas.users import CreateUser, User
# from sqlalchemy.sql import text

# sqlalchemy core의 기능을 이용한 가동성 좋은 동기식 CRUD
# user CRUD

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


# question CRUD

def create_question(db: Session, question: str) -> Question:
    sql = insert(QuestionModel).values(question=question).returning(QuestionModel.id)
    result = db.execute(sql)
    db.commit()
    new_question_id = result.fetchone().id

    if new_question_id is None:
        raise HTTPException(status_code=400, detail="Question Not Created")
    try:
        new_question = db.query(QuestionModel).filter(QuestionModel.id == new_question_id).one()
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Question Not Found")

    return Question.from_orm(new_question)

def get_question_id(db: Session, q_id: int) -> Question:
    sql = select(QuestionModel).where(QuestionModel.id == q_id)
    try:
        result = db.execute(sql).scalar_one()
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Question not found")

    return Question.from_orm(result)

def get_questions(db: Session, skip: int = 0, limit: int = 10) -> list[Question]:
    sql = select(QuestionModel).offset(skip).limit(limit)
    results = db.execute(sql).scalars().all()

    questions = []
    for question in results:
        questions.append(question)

    return questions

def update_question(db: Session,  q_id: int, update_question: str) -> Question:
    question_data = update_question.dict()
    sql = update(QuestionModel).where(QuestionModel.id == q_id).values(**question_data)
    db.execute(sql)
    db.commit()

    question = get_question_id(db, q_id)
    
    return question

def delete_question(db: Session, q_id: int) -> Question:
    question = get_question_id(db, q_id)

    sql = (
        delete(QuestionModel).
        where(QuestionModel.id == q_id)
    )
    db.execute(sql)
    db.commit()

    return question


# answer CR

def create_answer(db: Session, answer: CreateAnswer) -> Answer:
    sql = insert(AnswerModel).values(user_id=answer.user_id, question_id=answer.question_id, answer=answer.answer).returning(AnswerModel.id)
    result = db.execute(sql)
    db.commit()
    new_answer_id = result.fetchone().id

    if new_answer_id is None:
        raise HTTPException(status_code=400, detail="Answer Not Created")
    try:
        new_answer = db.query(AnswerModel).filter(AnswerModel.id == new_answer_id).one()
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Answer Not Found")

    return Answer.from_orm(new_answer)

def get_answers(db: Session, question_id: int, skip: int = 0, limit: int = 10) -> list[QuestionAnswer]:
    sql = select(AnswerModel).where(AnswerModel.question_id == question_id).offset(skip).limit(limit)
    result = db.execute(sql).scalars().all()

    answers = [answer.to_dict() for answer in result]
    # for answer in result:
    #     answers.append(QuestionAnswer.from_orm(answer))

    return answers


# staff CRUD

def create_staff(db: Session, staff: CreateStaff) -> Staff:
    sql = insert(StaffModel).values(nickname=staff.nickname, password=staff.password).returning(StaffModel.id)
    result = db.execute(sql)
    db.commit()
    new_staff_id = result.fetchone().id

    if new_staff_id is None:
        raise HTTPException(status_code=400, detail="Staff Not Created")
    try:
        new_staff = db.query(StaffModel).filter(StaffModel.id == new_staff_id).one()
        return Staff.from_orm(new_staff)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Staff Not Found")

def get_staff_id(db: Session, id: int) -> Staff:
    sql = select(StaffModel).where(StaffModel.id == id)
    try:
        result = db.execute(sql).scalar_one()
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Staff not found")

    return Staff.from_orm(result)

def update_staff(db: Session, id: int, staff: UpdateStaff) -> Staff:
    staff_data = staff.dict()
    sql = update(StaffModel).where(StaffModel.id == id).values(**staff_data)
    db.execute(sql)
    db.commit()

    staff = get_staff_id(db, id)
    
    return staff

def delete_staff(db: Session, id: int) -> Staff:
    staff = get_staff_id(db, id)

    sql = (
        delete(StaffModel).
        where(StaffModel.id == id)
    )
    db.execute(sql)
    db.commit()

    return staff