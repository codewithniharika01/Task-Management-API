from sqlalchemy.orm import Session

from app.tasks.models import Task
from app.tasks.schema import TaskCreate, TaskUpdate

from app.user.models import Users
from app.user.schema import UserCreate

from app.auth import hash_password


def create_task(
    db: Session,
    task: TaskCreate,
    user_id: int
):

    new_task = Task(
        title=task.title,
        description=task.description,
        user_id=user_id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


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