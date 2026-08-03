from agents.agent import Agent
from services.llm_service import LLMService

class AssistantAgent(Agent):
    def __init__(self):
        super().__init__(name="Assistant Agent",description="General purpose AI assistant.")
        self.llm_service = LLMService()

    def execute(self,task: str) -> str:
        return self.llm_service.chat(task)