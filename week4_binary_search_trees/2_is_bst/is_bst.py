import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 25)  # new thread will get stack of such size


# result = []
#
#
# def traverse(root):
#     if root == -1: return
#     traverse(left[root])
#     result.append(key[root])
#     traverse(right[root])
#     return result
#
#
# result = traverse(0)
# print("result= ", result)
# isBST = True
# for i in range(1, n):
#     if result[i] <= result[i - 1]:
#         isBST = False
#         break
# return isBST


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

    def all(node, proposition):
        if node == -1:
            return True
        else:
            return proposition(key[node]) and \
                   all(left[node], proposition) and \
                   all(right[node], proposition)

    def isBST(node):
        if node == -1:
            return True
        else:
            return all(left[node], lambda v: v < key[node]) and \
                   all(right[node], lambda v: key[node] <= v) and \
                   isBST(left[node]) and \
                   isBST(right[node])

    return isBST(0)


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
