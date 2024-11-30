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
    datetime: datetime.datetime
    department_id: int
    job_id: int

class Rawdata(BaseModel):
    job: Optional[List[Job]] = []
    department: Optional[List[Department]] = []
    hired_employee: Optional[List[HiredEmployee]] = []

#Define a basic route
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}

@app.post("/receive_data")
async def receive_data(data: Rawdata):
    try:
        # Insert data for jobs table
        if data.job:
            jobs_entries = [Job(**item.dict()) for item in data.job]

        # Insert data for departments table
        if data.department:
            department_entries = [Department(**item.dict()) for item in data.department]

        # Insert data for hired_employees table
        if data.hired_employee:
            hired_employee_entries = [HiredEmployee(**item.dict()) for item in data.hired_employee]

        return jobs_entries, department_entries, hired_employee_entries
        #return {"message": "Data received and saved successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail="Error while saving data: " + str(e))
