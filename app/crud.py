from sqlalchemy.orm import Session

from app.tasks.models import Task
from app.tasks.schema import TaskCreate, TaskUpdate

from app.user.models import Users
from app.user.schema import UserCreate

from app.auth import hash_password


# ---------- USER ----------

def create_user(db: Session, user: UserCreate):

    hashed_password = hash_password(user.password)

    db_user = Users(
        username=user.username,
        email=user.email,
        password=hashed_password
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_user_by_email(
    db: Session,
    email: str
):

    return db.query(Users).filter(
        Users.email == email
    ).first()



# ---------- TASK ----------

def create_task(
    db: Session,
    task: TaskCreate,
    user_id: int
):

    db_task = Task(
        title=task.title,
        description=task.description,
        user_id=user_id
    )

    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task



def get_all_tasks(
    db: Session,
    user_id: int
):

    return db.query(Task).filter(
        Task.user_id == user_id
    ).all()



def get_task(
    db: Session,
    task_id: int,
    user_id: int
):

    return db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == user_id
    ).first()



def update_task(db, task_id, task_data, user_id):

    task = db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == user_id
    ).first()

    if task is None:
        return None

    if task_data.title is not None:
        task.title = task_data.title

    if task_data.description is not None:
        task.description = task_data.description

    if task_data.completed is not None:
        task.completed = task_data.completed

    db.commit()
    db.refresh(task)

    return task

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
