import json
from pathlib import Path

from agents.agent import Agent
from models.execution_plan import ExecutionPlan
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
    ) -> ExecutionPlan:

        template = Path(
            "prompts/planner.txt"
        ).read_text(
            encoding="utf-8"
        )
        prompt = template.format(
            task=task
        )
        response = self.llm_service.chat(
            prompt
        )

        data = json.loads(response)

        return ExecutionPlan(**data)