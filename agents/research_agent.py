from pathlib import Path

from agents.agent import Agent
from models.agent_result import AgentResult
from services.llm_service import LLMService

class ResearchAgent(Agent[AgentResult]):
    def __init__(self):
        super().__init__(
            name="Research Agent",
            description="Researches a topic."
        )

        self.llm_service = LLMService()

    def execute(self, task) -> AgentResult:
        template = Path(
            "prompts/research.txt"
        ).read_text(
            encoding="utf-8"
        )
        prompt = template.format(
            task=task
        )
        response = self.llm_service.chat(
            prompt
        )
        return AgentResult(
            agent=self.name,
            task=task,
            success=True,
            content=response
        )