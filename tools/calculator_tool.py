from tools.tool import Tool

class CalculatorTool(Tool):
    def __init__(self):
        super().__init__(
            name="Calculator",
            description="Performs basic arithmetic calculations."
        )

    def execute(
            self,
            input_text: str
    ) -> str:
        try:
            result = eval(input_text)
            return str(result)
        except Exception:
            return "Invalid expression."