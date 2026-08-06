from pathlib import Path

from agents.agent import Agent
from services.llm_service import LLMService

class ReviewerAgent(Agent[str]):

    def __init__(self):
        super().__init__(
            name="Reviewer Agent",
            description="Reviews AI output."
        )

        self.llm_service = LLMService()

    def execute(
        self,
        task: str
    ) -> str:
        template = Path(
            "prompts/reviewer.txt"
        ).read_text(
            encoding="utf-8"
        )
        prompt = template.format(
            research_results=task
        )
        return self.llm_service.chat(
            prompt
        )