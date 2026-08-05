from abc import ABC, abstractmethod

class Tool(ABC):
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
            input_text: str
    ) -> str:
        """
        Execute the tool.
        """
        pass