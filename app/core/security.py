from datetime import datetime, timedelta, timezone
from jose import jwt
from passlib.context import CryptContext
import hashlib
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    sha = hashlib.sha256(password.encode()).hexdigest()
    return pwd_context.hash(sha)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    sha = hashlib.sha256(plain_password.encode()).hexdigest()
    return pwd_context.verify(sha, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({
        "exp": expire,
        "sub": data.get("sub")
    })

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)