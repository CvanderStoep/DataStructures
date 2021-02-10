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

    def max_node(node):
        if left[node] == -1 and right[node] == -1:
            return key[node]
        if left[node] == -1:
            return max(key[node], max_node(right[node]))
        if right[node] == -1:
            return max(key[node], max_node(left[node]))
        return max(key[node], max_node(left[node]), max_node(right[node]))

    def min_node(node):
        if left[node] == -1 and right[node] == -1:
            return key[node]
        if left[node] == -1:
            return min(key[node], min_node(right[node]))
        if right[node] == -1:
            return min(key[node], min_node(left[node]))
        return min(key[node], min_node(left[node]), min_node(right[node]))

    isBST = True
    for node in range(n):
        if left[node] == -1 and right[node] == -1:
            #  empty node
            pass
        elif left[node] == -1 and right[node] != -1:
            #  only right node
            if min_node(right[node]) < key[node]:
                isBST = False
        elif right[node] == -1 and left[node] != -1:
            #  only left node
            if max_node(left[node]) >= key[node]:
                isBST = False
        elif left[node] != -1 and right[node] != -1:
            #  left + right node
            if min_node(right[node]) < key[node] or max_node(left[node]) >= key[node]:
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


# def IsBinarySearchTree(j, mn, mx):
#     if not j in tree: return True
#     if tree[j][0] < mn or tree[j][0] > mx: return False
#     return IsBinarySearchTree(tree[j][1], mn, tree[j][0] - 1) and IsBinarySearchTree(tree[j][2], tree[j][0], mx)
#
#
# def main():
#     nodes = int(sys.stdin.readline().strip())
#     global tree
#     tree, int_max, int_min = {}, 2147483647, -2147483648
#     for i in range(nodes):
#         tree[i] = (list(map(int, sys.stdin.readline().strip().split())))
#     if IsBinarySearchTree(0, int_min, int_max):
#         print("CORRECT")
#     else:
#         print("INCORRECT")


threading.Thread(target=main).start()
