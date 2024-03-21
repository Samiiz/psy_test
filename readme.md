심리테스트를 위한 로컬환경에서의 프로젝트 세팅

1. dockerfile과 requirements.txt를 통한 빌드 성공
    - 하지만 alembic.ini와 env.py의 세부 설정 불가(지식의 부족)
    - 그리하여 로컬환경에서 기본 ini 세팅 후 진행하는것으로 변경
    - 로컬에 postgres를 설치하고 모든 권한을 가진 베이스 유저 생성 성공
    - 로컬기준 alembic 세팅은 성공적!

2. 모델 생성

```python
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    password = Column(String, nullable=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    is_staff = Column(Boolean, default=False)

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
```

3. 모델 수정
    - admin page를 위해 staff를 분리하려다 보니 기존 users 테이블에서 작업하는것은 좋지 않다고 판단하여 staff 테이블 생성 후 내용 분리

    ```python
    class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)

    class Staff(Base):
    __tablename__ ='staff'

    id = Column(String, primary_key=True, index=True)
    nickname = Column(String, nullable=False)
    password = Column(String, nullable=True)
    ```