import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 25)  # new thread will get stack of such size


def IsBinarySearchTree(tree):
    #  we will run an inorder traversal and return False as soon as a smaller element than the previous is found
    n = len(tree)
    if n == 0: return True
    key = []
    left = []
    right = []

    for i in range(n):
        key.append(tree[i][0])
        left.append(tree[i][1])
        right.append(tree[i][2])

    # DONE return min_integer / max_integer for empty nodes
    int_max, int_min = 2147483647, -2147483648

    def max_node(node):
        #  returns the maximum value of a node (and all it children)
        if node == -1:
            return int_min
        else:
            return max(key[node], max_node(left[node]), max_node(right[node]))

    def min_node(node):
        #  returns the minimum value of a node (and all it children)
        if node == -1:
            return int_max
        else:
            return min(key[node], min_node(left[node]), min_node(right[node]))

    isBST = True
    for node in range(n):
        if max_node(left[node]) < key[node] <= min_node(right[node]):
            pass
        else:
            isBST = False
    return isBST


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


if __name__ == "__main__":
    # main()

    threading.Thread(target=main).start()
