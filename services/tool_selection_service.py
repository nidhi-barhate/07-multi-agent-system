from pathlib import Path
import json

from schemas.tool_decision import ToolDecision
from services.llm_service import LLMService


class ToolSelectionService:

    def __init__(self):
        self.llm_service = LLMService()

    def select_tool(
            self,
            task: str
    ) -> ToolDecision:
    
        template = Path(
            "prompts/tool_selector.txt"
        ).read_text(
            encoding="utf-8"
        )

        prompt = template.replace(
            "{task}",
            task
        )
        response = self.llm_service.chat(prompt)

        data = json.loads(response)
        return ToolDecision(**data)