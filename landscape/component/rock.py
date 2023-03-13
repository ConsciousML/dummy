class Rock:
    def __init__(self, width, height, char):
        self.width = width
        self.height = height
        self.char = char

    def __str__(self) -> str:
        rock_str = ''
        for _ in range(self.height):
            for _ in range(self.width):
                rock_str += self.char
            rock_str += '\n'
        return rock_str
