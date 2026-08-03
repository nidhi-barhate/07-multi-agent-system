from fastapi import APIRouter
from agents.assistant_agent import AssistantAgent
from schemas.agent_request import AgentRequest
from schemas.agent_response import AgentResponse
router = APIRouter()
agent = AssistantAgent()

@router.post("/api/agent",response_model=AgentResponse)
def execute(request: AgentRequest):
    result = agent.execute(
        request.task
    )
    return AgentResponse(
        result=result
    )