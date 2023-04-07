"""Trunk component"""
from math import ceil

from landscape.component.abstract import Component

class Trunk(Component):
    """This class defines a trunk component of the landscape"""
    def __init__(self, height: int, char:str) -> None:
        """
        Args:
            height (int): height of the trunk.
            char (str): character to print the trunk.
        """
        super().__init__(height, char)
        self.height = height


    def __str__(self) -> str:
        """Return a string representation of the trunk"""
        rock_str = ''
        for _ in range(self.height):
            rock_str += self.char + '\n'
        return rock_str