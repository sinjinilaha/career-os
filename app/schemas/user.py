from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from uuid import UUID



class UserCreate(BaseModel):
    email: EmailStr
    password: str
    phone_number: Optional[str] = None
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: UUID
    email: EmailStr
    phone_number: str | None
    created_at: datetime
    class Config:
        from_attributes = True
