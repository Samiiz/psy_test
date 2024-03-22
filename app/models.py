from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)

class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, nullable=False)

class Answer(Base):
    __tablename__ = 'answers'

    id = Column(Integer, primary_key=True, index=True)
    answer = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    question_id = Column(Integer, ForeignKey('questions.id'))

class Staff(Base):
    __tablename__ ='staff'

    id = Column(String, primary_key=True, index=True)
    nickname = Column(String, nullable=False)
    password = Column(String, nullable=True)