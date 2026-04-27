from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskResponse

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


# Create Task
@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    new_task = Task(
        user_id=1,
        title=task.title,
        deadline=task.deadline,
        priority=task.priority,
        status="pending"
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task