class GameNode:
    def __init__(self, num_pennies, left=None, middle=None, right=None):
        self.num_pennies = num_pennies
        self.left, self.middle, self.right = left, middle, right

    def is_leaf(self):
        if self.num_pennies == 0:
            return True

        else:
            return False

    def num_leaves(self):
        if self.is_leaf():
            return 1

        if self.left and self.middle and self.right:
            return self.left.num_leaves() + self.middle.num_leaves() + self.right.num_leaves()

        elif self.left and self.middle:
            return self.left.num_leaves() + self.middle.num_leaves()

        elif self.middle and self.right:
            return self.middle.num_leaves() + self.right.num_leaves()

        elif self.left and self.right:
            return self.left.num_leaves() + self.right.num_leaves()

        elif self.left and not self.middle and not self.right:
            return self.left.num_leaves()

        elif self.middle and not self.left and not self.right:
            return self.middle.num_leaves()

        elif self.right and not self.left and not self.middle:
            return self.right.num_leaves()

class GameTree:
    def __init__(self, num_pennies):
        self._root = self.make_node(num_pennies)
        self._game_position = self._root

    def make_node(self, num_pennies):
        if num_pennies >= 3:
            node = GameNode(num_pennies, left=self.make_node(num_pennies-1), middle=self.make_node(num_pennies-2),
                            right=self.make_node(num_pennies-3))
            return node

        if num_pennies == 2:
            node = GameNode(num_pennies, left=self.make_node(num_pennies-1),
                            middle=self.make_node(num_pennies-2))

            return node

        if num_pennies == 1:
            node = GameNode(num_pennies, left=self.make_node(num_pennies-1))
            return node

        if num_pennies == 0:
            node = GameNode(num_pennies)
            return node

def main():
    first_node = GameNode(2)
    second_node = GameNode(1)
    third_node = GameNode(0)
    fourth_node = GameNode(0)

    first_node.left = second_node
    first_node.middle = third_node
    second_node.left = fourth_node

    print(first_node.num_leaves())

    tree = GameTree(5)
    print(tree._root.num_pennies)

if __name__ == '__main__':
    main()


