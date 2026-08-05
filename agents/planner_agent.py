from pathlib import Path

from agents.agent import Agent
from services.llm_service import LLMService


class PlannerAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Planner Agent",
            description="Creates execution plans."
        )
        self.llm_service = LLMService()

    def execute(
            self,
            task: str
    ) -> str:
        template = Path(
            "prompts/planner.txt"
        ).read_text(
            encoding="utf-8"
        )
        prompt = template.format(
            task=task
        )
        return self.llm_service.chat(
            prompt
        )