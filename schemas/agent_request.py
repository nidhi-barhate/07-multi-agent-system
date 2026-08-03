from pydantic import BaseModel

class AgentRequest(BaseModel):
    task: str