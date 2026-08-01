from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from app.tasks.schema import TaskCreate, TaskUpdate, TaskResponse
from app import crud
from app.dependencies import get_db
from fastapi import HTTPException
from app.dependencies import get_current_user


tasks = APIRouter()


@tasks.get("/tasks",response_model=list[TaskResponse]
)
def get_all_tasks(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    return crud.get_all_tasks(
        db,
        current_user.id
    )
@tasks.get("/tasks/{task_id}",response_model=TaskResponse)

def get_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    task = crud.get_task(
        db,
        task_id,
        current_user.id
    )

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task

@tasks.put("/tasks/{task_id}",response_model=TaskResponse)
def update_task(
    task_id: int,
    task: TaskUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
 updated_task = crud.update_task(
     db,
     task_id,
     task,
     current_user.id
     )
 if updated_task is None:
    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )

 return updated_task

@tasks.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    deleted_task = crud.delete_task(
        db,
        task_id,
        current_user.id
    )

    if deleted_task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {
        "message": "Task deleted successfully"
    }

@tasks.post(
    "/tasks",
    response_model=TaskResponse
)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return crud.create_task(
        db,
        task,
        current_user.id
    )


