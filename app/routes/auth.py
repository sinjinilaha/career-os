from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse, UserLogin
from app.core.security import hash_password, verify_password, create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# 🔹 REGISTER
@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):

    # ✅ Check if email already exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # ✅ Hash password
    hashed_pwd = hash_password(user.password)

    new_user = User(
        email=user.email,
        hashed_password=hashed_pwd,
        phone_number=user.phone_number
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# 🔹 LOGIN
@router.post("/login")
def login_user(user: UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Create JWT token
    token = create_access_token(data={"sub": str(db_user.id)})

    return {
        "access_token": token,
        "token_type": "bearer"
    }