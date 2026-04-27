from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)

    # Foreign key → links task to a user
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    title = Column(String, nullable=False)
    deadline = Column(DateTime, nullable=True)

    # Example: low / medium / high
    priority = Column(String, default="medium")

    # pending / completed
    status = Column(String, default="pending")

    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship (important for ORM navigation)
    user = relationship("User", back_populates="tasks")