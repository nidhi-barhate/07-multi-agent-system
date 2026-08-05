from agents.agent import Agent
from agents.planner_agent import PlannerAgent
from services.llm_service import LLMService
from services.tool_selection_service import ToolSelectionService
from tools.calculator_tool import CalculatorTool
from tools.time_tool import TimeTool
from tools.weather_tool import WeatherTool

class AssistantAgent(Agent):
    def __init__(self):
        super().__init__(name="Assistant Agent",description="General purpose AI assistant.")
        self.llm_service = LLMService()
        self.calculator_tool = CalculatorTool()
        self.weather_tool = WeatherTool()
        self.time_tool = TimeTool()
        self.tool_selection_service = ToolSelectionService() 
        self.planner_agent = PlannerAgent()
        
    def execute(
            self,
            task: str
    ) -> str:
        print(f"Executing task: {task}")
        decision = self.tool_selection_service.select_tool(task)
        print(f"Tool selected: {decision.tool}, Input: {decision.input}")
        if decision.tool == "calculator":
            return self.calculator_tool.execute(
                decision.input
            )

        if decision.tool == "weather":
            return self.weather_tool.execute(
                decision.input
            )

        if decision.tool == "time":
            return self.time_tool.execute(
                decision.input
            )
        return self.planner_agent.execute(task)