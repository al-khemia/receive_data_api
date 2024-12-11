from fastapi import Depends, FastAPI, Response, status, HTTPException
from sqlalchemy.orm import Session
from app import models
from app import schemas
from app import crud
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

# Create an instance of the FastAPI app
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Define a basic route
@app.post("/jobs", response_model=schemas.JobCreate)
def create_job(job: schemas.JobCreate, db: Session = Depends(get_db)):
    return crud.create_job(db=db, job=job)


@app.get("/")
def read_root():
    return {"message": "Welcome to Migrate Data API"}

# @app.post("/migrate_data")
# async def migrate_data(data: Rawdata):
#     try:
#         # Insert data for jobs table
#         if data.job:
#             jobs_entries = [Job(**item.dict()) for item in data.job]
#
#         # Insert data for departments table
#         if data.department:
#             department_entries = [Department(**item.dict()) for item in data.department]
#
#         # Insert data for hired_employees table
#         if data.hired_employee:
#             hired_employee_entries = [HiredEmployee(**item.dict()) for item in data.hired_employee]
#
#         return {"message": "Data migrated and saved successfully"}
#
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Error while saving data: " + str(e))
