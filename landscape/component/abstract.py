from abc import ABC, abstractmethod

class Component(ABC):
    def __init__(self, width, char):
        self.width = width
        self.char = char

    @abstractmethod
    def __str__(self) -> str:
        pass
