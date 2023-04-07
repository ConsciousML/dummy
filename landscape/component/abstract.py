"""Contain abstract classes of the components"""
from abc import ABC, abstractmethod

class Component(ABC):
    """This class defines the abstract class of the components of the landscape"""""
    def __init__(self, width: int, char: str):
        """
        Args:
            width (int): width of the component.
            char (str): character to print the component.
        """
        self.width = width
        self.char = char

    @abstractmethod
    def __str__(self) -> str:
        """Return a string representation of the component"""
        pass
