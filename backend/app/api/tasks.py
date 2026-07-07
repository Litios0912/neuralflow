from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import datetime

from app.database import get_db
from app.models.task import ScheduledTask
from app.models.user import User
from app.api.auth import get_current_user

router = APIRouter(prefix="/tasks", tags=["tasks"])

class TaskCreate(BaseModel):
    agent_id: int
    name: str
    schedule_type: str
    schedule_config: dict = {}
    input_data: dict = {}

class TaskResponse(BaseModel):
    id: int
    name: str
    schedule_type: str
    status: str
    last_run: datetime | None
    next_run: datetime | None

    class Config:
        from_attributes = True

@router.get("/", response_model=list[TaskResponse])
def list_tasks(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(ScheduledTask).filter(ScheduledTask.user_id == current_user.id).all()

@router.post("/", response_model=TaskResponse)
def create_task(task_data: TaskCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    task = ScheduledTask(
        user_id=current_user.id,
        agent_id=task_data.agent_id,
        name=task_data.name,
        schedule_type=task_data.schedule_type,
        schedule_config=task_data.schedule_config,
        input_data=task_data.input_data
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    task = db.query(ScheduledTask).filter(ScheduledTask.id == task_id, ScheduledTask.user_id == current_user.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"message": "Task deleted"}
