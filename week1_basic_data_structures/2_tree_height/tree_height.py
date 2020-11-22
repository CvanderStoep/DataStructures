# python3

import sys
import threading


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


def compute_height(n, parents):
    # Replace this code with a faster implementation
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
    print('height-naive= ', compute_height(n, parents))
    nodes = []  # this is the actual Tree; a list of Nodes
    root = None
    # n = 5
    for i in range(n):
        nodes.append(Node(number=i))
    # parents = [-1, 0, 4, 0, 3]
    for child_index in range(n):
        parent_index = parents[child_index]
        if parent_index == -1:
            root = child_index
        else:
            nodes[parent_index].add_child(nodes[child_index])

    # for i in range(n):
    #     ls = nodes[i].list_children_numbers()
    #     print('i, ls= ', i, ls)

    # make a BFS queue
    # put root on queue first
    # dequeue first element of queue and put all children on the queue
    # this will traverse through the queue layer by layer.

    print('nodes using LevelTraversal= ', LevelTraversal(root, nodes))
    print('height-using recursion= ', Height(nodes))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size
threading.Thread(target=main).start()
