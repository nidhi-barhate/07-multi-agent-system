from pathlib import Path

from agents.agent import Agent
from services.llm_service import LLMService

class ResearchAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Research Agent",
            description="Researches a topic."
        )

        self.llm_service = LLMService()

    def execute(
        self,
        task: str
    ) -> str:
        template = Path(
            "prompts/research.txt"
        ).read_text(
            encoding="utf-8"
        )
        prompt = template.format(
            task=task
        )
        return self.llm_service.chat(
            prompt
        )