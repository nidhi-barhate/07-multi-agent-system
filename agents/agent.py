from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class Agent(ABC, Generic[T]):
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
    ) -> T:
        pass