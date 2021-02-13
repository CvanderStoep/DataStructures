# python3

import sys


def precomputehash(S, m1 = 10 ** 9 + 7, m2 = 10 ** 9 + 9, x = 263):
    n = len(S)
    h1 = [0] * (n + 1)
    h2 = [0] * (n + 1)
    for i in range(1, n + 1):
        # there is an error in the description; s[i] should be s[i-1]
        h1[i] = (x * h1[i - 1] + ord(S[i - 1])) % m1
        h2[i] = (x * h2[i - 1] + ord(S[i - 1])) % m2
    # print(h1, h2)
    return h1, h2, m1, m2, x


class Solver:
    def __init__(self, s):
        self.s = s

    def ask(self, a, b, l):
        return s[a:a + l] == s[b:b + l]


if __name__ == '__main__':
    s = sys.stdin.readline()
    h1, h2, m1, m2, x = precomputehash(s)
    # m1 = 10 ** 9 + 7
    # m2 = 10 ** 9 + 9
    # x = 263

    q = int(sys.stdin.readline())
    solver = Solver(s)
    for i in range(q):
        a, b, l = map(int, sys.stdin.readline().split())
        H1a = h1[a + l] % m1 - (x ** l * h1[a]) % m1
        H1b = h1[b + l] % m1 - (x ** l * h1[b]) % m1
        H2a = h2[a + l] % m2 - (x ** l * h2[a]) % m2
        H2b = h2[b + l] % m2 - (x ** l * h2[b]) % m2
        # print(H1a, H1b, H2a, H2b)
        print("Yes" if solver.ask(a, b, l) else "No")
        print("Yes2" if H1a == H1b and H2a == H2b else "No2")
