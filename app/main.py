from typing import Union
from routers.users import router as user_routers
from fastapi import FastAPI

app = FastAPI()


app.include_router(user_routers, prefix='/api/v1/users', tags=['User'])

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", reload=True)