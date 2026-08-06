from pydantic import BaseModel

class AgentResult(BaseModel):
    agent: str
    task: str
    success: bool
    content: str