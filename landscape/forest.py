from landscape.component.tree import Tree

class Forest:
    def __init__(self) -> None:
        self.list_components = []

    def add(self, object) -> None:
        self.list_components.append(object)

    def __str__(self) -> str:
        forest_str = ''
        for component in self.list_components:
            forest_str += str(component)
        return forest_str