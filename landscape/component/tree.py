"""Tree component"""
from math import ceil

from landscape.component.abstract import Component

class Tree(Component):
    """This class defines a tree component of the landscape"""
    def __init__(self, width: int, char: str) -> None:
        """
        Args:
            width (int): width of the tree.
            char (str): character to print the tree.
        """
        super().__init__(width, char)

    def __str__(self) -> str:
        """Return a string representation of the tree"""
        tree_shape = ''

        half_width = ceil(self.width / 2)
        for row in range(self.width):
            for _ in range(half_width - row + 1):
                tree_shape += ' '
            tree_shape += ' '.join([self.char for _ in range(row + 1)]) + '\n'
        return tree_shape
