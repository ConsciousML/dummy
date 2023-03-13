from math import ceil

class Tree:
    def __init__(self, width, leaf_char):
        self.width = width
        self.leaf_char = leaf_char

    def __str__(self) -> str:
        tree_shape = ''

        half_width = ceil(self.width / 2)
        for row in range(self.width):
            for _ in range(half_width - row + 1):
                tree_shape += ' '
            tree_shape += ' '.join([self.leaf_char for _ in range(row + 1)]) + '\n'
        return tree_shape
