from sqlalchemy import Column, DateTime, Integer, String
from app.database import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    job = Column(String(6), nullable=False)