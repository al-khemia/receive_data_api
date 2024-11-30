import datetime as datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional

# Create an instance of the FastAPI app
app = FastAPI()

# In-memory "database"
jobs_db = []
departments_db = []
hired_employees_db = []

# --- pydantic models --- #
# Model for Job table
class Job(BaseModel):
    id: int
    job: str

# Model for Department table
class Department(BaseModel):
    id: int
    department: str

# Model for Hired Employees table
class HiredEmployee(BaseModel):
    id: int
    name: str
    #datetime: datetime
    department_id: int
    job_id: int

#Define a basic route
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}

@app.post("/receive_data")
async def receive_data(job: Job):
    # Create a new user with an auto-incremented ID
    id = len(jobs_db) + 1
    new_job = {"id": id, **job.dict()}
    return new_job
