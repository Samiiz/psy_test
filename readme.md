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

4. 스키마 생성
    - [스키마](app/schemas)
    - 공식 문서에 맞춰서 orm_mode = True -> from_attributes=True 로 변경

5. 라우터 생성
    - [라우터](app/routers)
    - [users](app/routers/users.py)
        - post 추가

6. CRUD(sql)용 sql.py생성
    -[SQL](app/crud/sql.py)

7. Alembic 관련 사항 수정
    - 도커에 올렸을때 지속적인 Alembic 오류로 공식문서 및 다양한 블로그 확인  
      그 결과 [alembic.ini](app/alembic.ini)의 위치가 내기준 프로젝트 최상위 디렉토리가 아니라  
      app에 위치해야 하며 그에따른 `script_location` 을 수정해줘야 했으며  
      [env.py](app/alembic/env.py)와 연결되어있는 [models.py](app/models.py), [database.py](app/database.py)의 상대적인 경로를 변경하고  
      그로인해 [alembic.ini](app/alembic.ini)관련 오류 해결

8. 도커 컴포즈 수정
    - 기존 코드  
    ```yml
    services:
      app:
          build: .
          ports:
          - "8000:8000"
          depends_on:
          - db
          environment:
          DATABASE_URL: postgresql+psycopg2://"username":"password"@"host"/"dbname"
          command: >
          sh -c "python3 main.py"
    ```
    이렇게 애플리케이션 서비스를 `app`이라고 지정하고 DATABASE_URL을 따로 받아왔다  
    하지만 `sqlalchemy.exc.OperationalError: (psycopg2.OperationalError)`  
    오류 발생! 구글링과 공식문서를 확인 한 결과 많은 사람들이 서비스를 `web`으로 지정하였다.

    그래서 변경한것이 
    ```yml
    services:
      web:
        build: .
        command: >
          sh -c "alembic revision --autogenerate -m 'docker-compose bulid' && \
                 alembic upgrade head && \
                 uvicorn main:app --host 0.0.0.0 --port 8000"

        volumes:
          - ./app:/app
        ports:
          - "8000:8000"
        depends_on:
          - db
    ```
    이렇게 병경하니 잘 되었다!

    다시 공부해보니 `sqlalchemy.exc.OperationalError: (psycopg2.OperationalError)`   
    이 오류는 내가 host를 `localhost`로 설쟁해서 문제가 생긴 것이였다.  
    도커에 올릴땐 보통 이미지를 생성해서 진행하기 때문에 host는 db로 진행 해야한다. 