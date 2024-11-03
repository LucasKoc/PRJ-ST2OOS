from fastapi import HTTPException
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

from api.core.settings import Settings

# Base class for SQLAlchemy models
Base = declarative_base()

engine = create_engine(Settings.DATABASE_FULL_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    if SessionLocal is None:
        raise HTTPException(status_code=500, detail="Database session not initialized.")
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
