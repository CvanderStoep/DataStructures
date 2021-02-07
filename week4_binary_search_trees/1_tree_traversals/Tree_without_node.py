class Tree:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert(self, value):
        if self.value is None:
            self.value = value
            return
        else:
            if value < self.value:
                if self.left_child is None:
                    self.left_child = Tree(value)
                else:
                    self.left_child.insert(value)
            elif value > self.value:
                if self.right_child is None:
                    self.right_child = Tree(value)
                else:
                    self.right_child.insert(value)
            else:
                print("Value is already existing in Tree.")

    def print_tree(self):
        result = []

        if self.value is None:
            return []

        if self.left_child is not None:
            result += self.left_child.print_tree()

        result += [self.value]

        if self.right_child is not None:
            result += self.right_child.print_tree()

        return result


def main():
    tree = Tree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(20)
    tree.insert(15)
    tree.insert(9)
    tree.insert(14)
    tree.insert(7)
    tree.insert(23)
    tree.insert(45)
    tree.insert(91)

    print(tree.print_tree())

    print("done")


if __name__ == "__main__":
    main()
