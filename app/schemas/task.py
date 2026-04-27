from pydantic import BaseModel
from datetime import datetime
from typing import Optional


# Base schema (common fields)
class TaskBase(BaseModel):
    title: str
    deadline: Optional[datetime] = None
    priority: Optional[str] = "medium"


# For creating a task (input)
class TaskCreate(TaskBase):
    pass


# For response (output)
class TaskResponse(TaskBase):
    id: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True