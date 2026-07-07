from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.api import auth, agents, tasks
from app.services.scheduler import start_scheduler
from app.agents import chat_agent, web_scraper, content_generator, data_analyzer
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="NeuralFlow API",
    description="AI Automation Platform API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(agents.router)
app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message": "NeuralFlow API is running", "version": "1.0.0"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.on_event("startup")
def on_startup():
    try:
        start_scheduler()
        logger.info("Scheduler started successfully")
    except Exception as e:
        logger.warning(f"Scheduler not available: {e}")

@app.on_event("shutdown")
def on_shutdown():
    from app.services.scheduler import scheduler
    scheduler.shutdown(wait=False)
