# python3

import sys, os
import threading


def test_files():
    """"This routine runs all the test files in the test directory"""
    os.chdir('./tests')
    for f in os.listdir():
        file_name, f_ext = os.path.splitext(f)
        file = open(f, "r")
        if f_ext != ".a":
            n = int(file.readline())
            input_text = file.readline()  # .strip()
            parents = list(map(int, input_text.split()))
            computed_height_naive = compute_height_naive(n, parents)
            print(f, 'height naive= ', computed_height_naive)

            root, nodes = convert_parent_child(n, parents)
            computed_height_recursion = Height([nodes[root]])
            print(f, 'height using recursion= ',
                  computed_height_recursion)
            computed_height_level_traversal = LevelTraversal(root, nodes)
            print(f, 'height using level traversal= ',
                  computed_height_level_traversal)

        else:
            output_height = int(file.readline())
            print(f, computed_height_naive, computed_height_recursion,computed_height_level_traversal , output_height)
            if not (computed_height_naive == output_height == computed_height_recursion == computed_height_level_traversal):
                print(f, 'wrong answer!')  # something is wrong


class Node:
    def __init__(self, number=None, children=None, level=1):
        self.children = []
        self.number = number
        self.level = level
        if children is not None:
            for child in children:
                self.add_child(child)

    def add_child(self, node):
        # assert isinstance(node, Node)
        self.children.append(node)

    def list_children_numbers(self):
        ls = []
        if self.children is not None:
            for child in self.children:
                ls.append(child.number)
        return ls


def compute_height_naive(n, parents):
    # Replace this code with a faster implementation
    """Naive implementation of the height of a Tree using only parents definition for the nodes"""
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height


def LevelTraversal(root, nodes):
    """Print all nodes moving through the levels using BFS"""
    if root is None:
        return []
    BFS_queue = [root]
    all_nodes = []
    max_height = 0
    while len(BFS_queue) != 0:
        node_number = BFS_queue.pop(0)
        all_nodes.append(node_number)
        list_children_nodes = nodes[node_number].children
        if len(list_children_nodes) != 0:
            for child in list_children_nodes:
                BFS_queue.append(child.number)
                child.level = nodes[node_number].level + 1
                max_height = max(child.level, max_height)
    return max_height #, all_nodes


def Height(nodes):
    if len(nodes) == 0:
        return 0
    return 1 + max(Height(node.children) for node in nodes)


def convert_parent_child(n, parents):
    nodes = []  # this is the actual Tree; a list of Nodes
    root = None
    for i in range(n):
        nodes.append(Node(number=i))
    for child_index in range(n):
        parent_index = parents[child_index]
        if parent_index == -1:
            root = child_index
        else:
            nodes[parent_index].add_child(nodes[child_index])
    return root, nodes


def main():
    test_files()
    #  read input, string of parents per node
    n = int(input("give number of nodes: \n"))
    parents = list(map(int, input("give list of nodes: \n").split()))

    # print('height-naive= ', compute_height_naive(n, parents))

    #  input string denotes all parents, need to transform this to children
    root, nodes = convert_parent_child(n, parents)

    print('height using LevelTraversal (BFS)= ', LevelTraversal(root, nodes))
    print('height using recursion (DFS)= ', Height([nodes[root]]))  # the tree is defined using the starting Node


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size
threading.Thread(target=main).start()
