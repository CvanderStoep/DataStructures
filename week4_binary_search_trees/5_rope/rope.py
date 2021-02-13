import sys


class Rope:
    def __init__(self, s):
        self.s = s

    def result(self):
        return self.s

    def process(self, i, j, k):
        # This uses standard string slicing & dicing
        # it does not use the splay tree as intended in the course!
        s_cut = self.s[i:j + 1]
        s_new = self.s[:i] + self.s[j + 1:]
        s_return = s_new[:k] + s_cut + s_new[k:]
        self.s = s_return


def main():
    rope = Rope(sys.stdin.readline().strip())
    q = int(sys.stdin.readline())
    for _ in range(q):
        i, j, k = map(int, sys.stdin.readline().strip().split())
        rope.process(i, j, k)
    print(rope.result())


if __name__ == "__main__":
    main()
