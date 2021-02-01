# python3

import sys, threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def __init__(self):
        # below is used for inorder_bad_alternative
        self.result2 = []

    def read(self):
        file = open('./tests/2', "r")
        self.n = int(file.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            input_text = file.readline()  # .strip()
            [a, b, c] = (map(int, input_text.split()))
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c


    def inOrder(self):
        result = []

        def traverse(root):
            if root == -1: return
            traverse(self.left[root])
            result.append(self.key[root])
            traverse(self.right[root])

        traverse(0)

        # Finish the implementation
        # You may need to add a new recursive method to do that

        return result

    def inOrder_bad_alternative(self, root):

        if root == -1: return
        self.inOrder_bad_alternative(self.left[root])
        self.result2.append(self.key[root])
        self.inOrder_bad_alternative(self.right[root])


        # Finish the implementation
        # You may need to add a new recursive method to do that

        return self.result2

    def preOrder(self):
        self.result = []

        def traverse(root):
            if root != -1:
                self.result.append(self.key[root])
                traverse(self.left[root])
                traverse(self.right[root])

        traverse(0)

        # Finish the implementation
        # You may need to add a new recursive method to do that

        return self.result

    def postOrder(self):
        self.result = []

        def traverse(root):
            if root != -1:
                traverse(self.left[root])
                traverse(self.right[root])
                self.result.append(self.key[root])

        traverse(0)

        # Finish the implementation
        # You may need to add a new recursive method to do that

        return self.result


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.inOrder_bad_alternative(root=0)))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()
