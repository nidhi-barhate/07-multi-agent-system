from concurrent.futures import ThreadPoolExecutor

from agents.agent import Agent
from agents.planner_agent import PlannerAgent
from agents.research_agent import ResearchAgent
from agents.reviewer_agent import ReviewerAgent
from services.llm_service import LLMService
from services.tool_selection_service import ToolSelectionService
from tools.calculator_tool import CalculatorTool
from tools.time_tool import TimeTool
from tools.weather_tool import WeatherTool

class OrchestratorAgent(Agent):
    def __init__(self):
        super().__init__(name="Orchestrator Agent",description="Manages and coordinates other agents.")
        self.llm_service = LLMService()
        self.calculator_tool = CalculatorTool()
        self.weather_tool = WeatherTool()
        self.time_tool = TimeTool()
        self.tool_selection_service = ToolSelectionService() 
        self.planner_agent = PlannerAgent()
        self.research_agent = ResearchAgent()
        self.reviewer_agent = ReviewerAgent()
        
    def execute(
            self,
            task: str
    ) -> str:
        print("=" * 80)
        print("ORCHESTRATOR")
        print("=" * 80)
        print("Task:", task)
        decision = self.tool_selection_service.select_tool(task)
        print("Selected Tool:", decision.tool)

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
        print("=" * 80)
        print("PLANNER")
        print("=" * 80)
        planning_result = self.planner_agent.execute(task)
        print(f"Planning result: {planning_result}")

        print("=" * 80)
        print("RESEARCH")
        print("=" * 80)
        # research_result = []
        # for step in planning_result.steps:
        #     result = self.research_agent.execute(step)
        #     research_result.append(result)

        research_result = []
        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = []
            for step in planning_result.steps:
                future = executor.submit(
                    self.research_agent.execute,
                    step
                )
                futures.append(future)

            for future in futures:
                result = future.result()
                research_result.append(result)    
        print(f"Research result: {research_result}")
        
        print("=" * 80)
        print("REVIEWER")
        print("=" * 80)
        research_merged_content = "\n\n".join(
            f"Task: {result.task}\n"
            f"Research:\n{result.content}"
            for result in research_result
        )
        review_result = self.reviewer_agent.execute(research_merged_content)
        print(f"Review result: {review_result}")
        return review_result