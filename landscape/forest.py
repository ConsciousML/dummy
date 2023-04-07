"""Class Forest to store the components of the landscape"""
from landscape.component.abstract import Component

class Forest:
    """This class contains a list of components of the landscape"""
    def __init__(self) -> None:
        """
        Attributes:
            list_components (list): list of the components of the landscape.
        """
        self.list_components = []

    def add(self, object: Component) -> None:
        """Add a component to the list of components
        
        Args:
            object (Component): component to add to the list of components.
        """
        if not isinstance(object, Component):
            raise TypeError('Only objects of type Component can be added to the forest')
        self.list_components.append(object)

    def __str__(self) -> str:
        """Return a string representation of the forest"""
        forest_str = ''
        for component in self.list_components:
            forest_str += str(component)
        return forest_str