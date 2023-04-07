"""Rock component module."""
from landscape.component.abstract import Component

class Rock(Component):
    """This a class to represent a rock component of the landscape"""
    def __init__(self, width: int, height: int, char: str):
        """
        Args:
            width (int): width of the rock.
            height (int): height of the rock.
            char (str): character to print the rock.
        """
        super().__init__(width, char)
        self.height = height

    def __str__(self) -> str:
        """Return a string representation of the rock"""
        rock_str = ''
        for _ in range(self.height):
            for _ in range(self.width):
                rock_str += self.char
            rock_str += '\n'
        return rock_str
