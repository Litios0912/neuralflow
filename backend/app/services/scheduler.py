from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.task import ScheduledTask
from datetime import datetime
import logging

logger = logging.getLogger(__name__)
scheduler = BackgroundScheduler()

def execute_task(task_id: int):
    db = SessionLocal()
    try:
        task = db.query(ScheduledTask).filter(ScheduledTask.id == task_id).first()
        if task:
            logger.info(f"Executing task {task.id}: {task.name}")
            task.last_run = datetime.utcnow()
            db.commit()
    except Exception as e:
        logger.error(f"Task {task_id} failed: {e}")
    finally:
        db.close()

def start_scheduler():
    db = SessionLocal()
    try:
        tasks = db.query(ScheduledTask).filter(ScheduledTask.status == "active").all()
        for task in tasks:
            if task.schedule_type == "interval":
                scheduler.add_job(
                    execute_task,
                    IntervalTrigger(seconds=task.schedule_config.get("seconds", 3600)),
                    args=[task.id],
                    id=f"task_{task.id}"
                )
            elif task.schedule_type == "daily":
                scheduler.add_job(
                    execute_task,
                    CronTrigger(hour=task.schedule_config.get("hour", 9)),
                    args=[task.id],
                    id=f"task_{task.id}"
                )
    finally:
        db.close()
    scheduler.start()
    logger.info("Scheduler started")
