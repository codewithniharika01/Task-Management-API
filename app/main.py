from fastapi import FastAPI

from app.db import engine, Base

from app.user.models import Users
from app.tasks.models import Task

from app.tasks.router import tasks
from app.user import router as user_router


app = FastAPI()


Base.metadata.create_all(bind=engine)


app.include_router(tasks)
app.include_router(user_router.router)