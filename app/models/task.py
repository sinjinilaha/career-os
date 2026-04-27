import uuid

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    # Foreign key → links task to a user
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    title = Column(String, nullable=False)
    deadline = Column(DateTime, nullable=True)

    # Example: low / medium / high
    priority = Column(String, default="medium")

    # pending / completed
    status = Column(String, default="pending")

    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship (important for ORM navigation)
    user = relationship("User", back_populates="tasks")