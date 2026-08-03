from abc import ABC, abstractmethod

class Agent(ABC):
    def __init__(
            self,
            name: str,
            description: str
    ):
        self.name = name
        self.description = description

    @abstractmethod
    def execute(
            self,
            task: str
    ) -> str:
        """
        Execute a task.
        """
        pass