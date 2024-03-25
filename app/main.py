from typing import Union
from routers.users import router as user_routers
from routers.questions import router as question_routers
from routers.answers import router as answer_routers
from routers.pages import router as main_routers
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(user_routers, prefix='/api/v1/users', tags=['User'])
app.include_router(question_routers, prefix='/api/v1/questions', tags=['Question'])
app.include_router(answer_routers, prefix='/api/v1/answers', tags=['Answer'])

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", reload=True)