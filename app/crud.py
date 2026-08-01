print("CRUDAAA LOADED")

from sqlalchemy.orm import Session

from app.tasks.models import Task
from app.tasks.schema import  TaskUpdate

from app.user.models import User
from app.user.schema import UserCreate
from app.auth import hash_password


def create_user(db, user: UserCreate):
    hashed_password = hash_password(user.password)

    db_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

def get_task(
    db: Session,
    task_id: int,
    user_id: int
):

    return db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == user_id
    ).first()


def update_task(
    db: Session,
    task_id: int,
    task: TaskUpdate,
    user_id: int
):

    existing_task = db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == user_id
    ).first()


    if existing_task is None:
        return None


    existing_task.title = task.title
    existing_task.description = task.description

    db.commit()
    db.refresh(existing_task)

    return existing_task

def delete_task(
    db: Session,
    task_id: int,
    user_id: int
):

    task = db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == user_id
    ).first()


    if task is None:
        return None


    db.delete(task)
    db.commit()

    return task

def get_user_by_email(
    db: Session,
    email: str
):
    return db.query(User).filter(
        User.email == email
    ).first()