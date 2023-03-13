from landscape.tree import Tree
from landscape.forest import Forest

if __name__ == '__main__':
    tree_star = Tree(5, '*')
    tree_o = Tree(3, 'o')

    forest = Forest()
    forest.add(tree_star)
    forest.add(tree_o)

    print(forest)
