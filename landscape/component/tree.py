from math import ceil

class Tree:
    def __init__(self, width, char):
        self.width = width
        self.char = char

    def __str__(self) -> str:
        tree_shape = ''

        half_width = ceil(self.width / 2)
        for row in range(self.width):
            for _ in range(half_width - row + 1):
                tree_shape += ' '
            tree_shape += ' '.join([self.char for _ in range(row + 1)]) + '\n'
        return tree_shape
