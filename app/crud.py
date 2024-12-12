from sqlalchemy.orm import Session
from app import models
from app import schemas

def create_job(db: Session, job: schemas.JobCreate):
    print(job)
    print(type(job))
    new_job = models.Job(**job.dict())
    db.add(new_job)
    db.commit()
    #db.refresh(new_job)
    return new_job