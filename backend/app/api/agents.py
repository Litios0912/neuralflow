from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional

from app.database import get_db
from app.models.agent import Agent
from app.models.user import User
from app.api.auth import get_current_user
from app.agents.base import AgentFactory

router = APIRouter(prefix="/agents", tags=["agents"])

class AgentCreate(BaseModel):
    name: str
    type: str
    description: str = ""
    config: dict = {}

class AgentResponse(BaseModel):
    id: int
    name: str
    type: str
    description: str
    config: dict

    class Config:
        from_attributes = True

class AgentRunRequest(BaseModel):
    input: str
    config: Optional[dict] = None

class AgentRunResponse(BaseModel):
    output: str
    agent_name: str
    agent_type: str

@router.get("/", response_model=list[AgentResponse])
def list_agents(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Agent).filter(Agent.user_id == current_user.id).all()

@router.post("/", response_model=AgentResponse)
def create_agent(agent_data: AgentCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    agent = Agent(
        user_id=current_user.id,
        name=agent_data.name,
        type=agent_data.type,
        description=agent_data.description,
        config=agent_data.config
    )
    db.add(agent)
    db.commit()
    db.refresh(agent)
    return agent

@router.get("/types")
def get_agent_types():
    return {
        "agent_types": AgentFactory.get_available_types()
    }

@router.post("/{agent_id}/run", response_model=AgentRunResponse)
def run_agent(agent_id: int, request: AgentRunRequest, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    agent = db.query(Agent).filter(Agent.id == agent_id, Agent.user_id == current_user.id).first()
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    agent_instance = AgentFactory.create_agent(agent.type, agent.config)
    output = agent_instance.run(request.input)
    return AgentRunResponse(output=output, agent_name=agent.name, agent_type=agent.type)

@router.delete("/{agent_id}")
def delete_agent(agent_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    agent = db.query(Agent).filter(Agent.id == agent_id, Agent.user_id == current_user.id).first()
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    db.delete(agent)
    db.commit()
    return {"message": "Agent deleted"}
