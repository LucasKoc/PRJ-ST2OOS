from typing import Optional
from pydantic import BaseModel
from sqlalchemy import Column, String, Integer, Boolean, JSON

from api.core.settings import Settings
from api.database.database import Base

class CourseModel(BaseModel):
    course_id: str
    course_name: str
    teacher_id: str


class CourseModelDB(Base):
    __tablename__ = "courses"
    __table_args__ = {"schema": Settings.POSTGRES_SCHEMA}

    course_id = Column(String, primary_key=True, index=True)
    course_name = Column(String)
    teacher_id = Column(String)
