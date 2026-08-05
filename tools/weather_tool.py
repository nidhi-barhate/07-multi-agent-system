from tools.tool import Tool

class WeatherTool(Tool):
    def __init__(self):
        super().__init__(
            name="weather",
            description="Returns dummy weather information."
        )
    def execute(
            self,
            input_text: str
    ) -> str:
        return (
            "Weather is sunny, "
            "31°C."
        )