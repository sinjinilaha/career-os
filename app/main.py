from fastapi import FastAPI
from sqlalchemy import text
from app.database import Base, engine
from app.models import User
from app.routes import auth

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CareerOS API",
    description="Backend API for CareerOS system",
    version="1.0.0"
)
app.include_router(auth.router)

@app.get("/")
def health_check():
    return {"status": "CareerOS Backend Running"}


@app.get("/db-test")
def test_db():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            return {"db_response": result.scalar()}
    except Exception as e:
        return {"error": str(e)}
    