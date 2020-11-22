# python3

import sys, os
import threading


# TODO run all test files
# def test_files():
#     os.chdir('./tests')
#     for f in os.listdir():
#         file_name, f_ext = os.path.splitext(f)
#         file = open(f,"r")
#         if f_ext != ".a":
#             input_text = file.read().strip()
#             mismatch = find_mismatch(input_text)
#         else:
#             output_text = file.read().strip()
#             # print(input_text)
#             # print(mismatch)
#             # print(output_text)
#             if "Success" in output_text and "Success" in mismatch: #both give success
#                 print(f, "pass")
#             elif str(output_text) == str(mismatch[0]): #both give same answer
#                 print(f, "pass")
#             else:
#                 print(f, 'wrong answer!') #something is wrong


class Node:
    def __init__(self, number=None, parent=None, children=None):
        self.parent = parent
        self.children = []
        self.number = number
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
    while len(BFS_queue) != 0:
        node = BFS_queue.pop(0)
        all_nodes.append(node)
        ls = nodes[node].list_children_numbers()
        if len(ls) != 0:
            for child in ls:
                BFS_queue.append(child)
    return all_nodes


def Height(nodes):
    if len(nodes) == 0:
        return 0
    max_height = 0
    for node in nodes:
        max_height = max(max_height, Height(node.children))
    return 1 + max_height


def main():
    n = int(input("give number of nodes: \n"))
    parents = list(map(int, input("give list of nodes: \n").split()))
    print('height-naive= ', compute_height_naive(n, parents))
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

    print('nodes using LevelTraversal= ', LevelTraversal(root, nodes))
    print('height-using recursion= ', Height([nodes[root]]))  # the tree is defined using the starting Node


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size
threading.Thread(target=main).start()
