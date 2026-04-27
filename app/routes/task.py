from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from uuid import UUID
from app.database import get_db
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskResponse
from app.core.deps import get_current_user

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


# Create Task

@router.post("/", response_model=TaskResponse)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: UUID = Depends(get_current_user)
):
    new_task = Task(
        user_id=current_user,
        title=task.title,
        deadline=task.deadline,
        priority=task.priority,
        status="pending"
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task
@router.get("/", response_model=list[TaskResponse])
def get_tasks(
    db: Session = Depends(get_db),
    current_user: UUID = Depends(get_current_user)
    ):
    tasks = db.query(Task).filter(Task.user_id == current_user).all()
    return tasks