from landscape.component.abstract import Component

class Rock(Component):
    def __init__(self, width, height, char):
        super().__init__(width, char)
        self.height = height

    def __str__(self) -> str:
        rock_str = ''
        for _ in range(self.height):
            for _ in range(self.width):
                rock_str += self.char
            rock_str += '\n'
        return rock_str
