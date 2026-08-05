from datetime import datetime
from tools.tool import Tool


class TimeTool(Tool):
    def __init__(self):
        super().__init__(
            name="time",
            description="Returns current system time."
        )

    def execute(
            self,
            input_text: str
    ) -> str:
        return datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )