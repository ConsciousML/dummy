from landscape.component.tree import Tree
from landscape.component.abstract import Component

class Forest:
    def __init__(self) -> None:
        self.list_components = []

    def add(self, object) -> None:
        if not isinstance(object, Component):
            raise TypeError('Only objects of type Component can be added to the forest')
        self.list_components.append(object)

    def __str__(self) -> str:
        forest_str = ''
        for component in self.list_components:
            forest_str += str(component)
        return forest_str