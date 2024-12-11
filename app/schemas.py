from typing import Optional
from pydantic import BaseModel
from datetime import datetime
# --- pydantic models --- #
# Model for Job table

class JobBase():
    job: str

class JobCreate(JobBase):
    pass

# Model for Department table
class Department(BaseModel):
    id: int
    department: str

# Model for Hired Employees table
class HiredEmployee(BaseModel):
    id: int
    name: str
    datetime: datetime
    department_id: int
    job_id: int