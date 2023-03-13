from landscape.tree import Tree

class Forest:
    def __init__(self) -> None:
        self.list_objects = []

    def add(self, object) -> None:
        self.list_objects.append(object)

    def __str__(self) -> str:
        forest_str = ''
        for object in self.list_objects:
            forest_str += str(object)
        return forest_str