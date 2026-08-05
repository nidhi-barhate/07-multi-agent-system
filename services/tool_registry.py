from tools.calculator_tool import CalculatorTool
from tools.tool import Tool

class ToolRegistry:
    def __init__(self):
        self.tools: dict[str, Tool] = {}
        self.register(
            CalculatorTool()
        )

    def register(
            self,
            tool: Tool
    ) -> None:
        self.tools[tool.name] = tool

    def get_tool(
            self,
            tool_name: str
    ) -> Tool | None:
        return self.tools.get(tool_name)

    def get_all_tools(
            self
    ) -> list[Tool]:
        return list(
            self.tools.values()
        )

    def get_tool_names(
            self
    ) -> list[str]:
        return list(
            self.tools.keys()
        )