# python3

import sys
from collections import namedtuple

Answer = namedtuple('answer_type', 'i j len')


def precomputehash(S):
    n = len(S)
    m1 = 10 ** 9 + 7
    m2 = 10 ** 9 + 9
    x = 263
    h1 = [0] * (n + 1)
    h2 = [0] * (n + 1)
    for i in range(1, n + 1):
        # there is an error in the description; s[i] should be s[i-1]
        h1[i] = (x * h1[i - 1] + ord(S[i - 1])) % m1
        h2[i] = (x * h2[i - 1] + ord(S[i - 1])) % m2
    # print(h1, h2)
    return h1, h2


def solve(s, t):
    ans = Answer(0, 0, 0)
    for i in range(len(s)):
        for j in range(len(t)):
            for l in range(min(len(s) - i, len(t) - j) + 1):
                if (l > ans.len) and (s[i:i + l] == t[j:j + l]):
                    ans = Answer(i, j, l)
    return ans


if __name__ == '__main__':
    s, t = map(str, sys.stdin.readline().split())
    m1 = 10 ** 9 + 7
    m2 = 10 ** 9 + 9
    x = 263
    found = False
    for k in range(min(len(s), len(t)), 0, -1):
        n = len(s)
        h1, h2 = precomputehash(s)
        Hsk = [0] * (n - k + 1)
        for i in range(0, n - k + 1):
            Hsk[i] = h1[i + k] % m1 - (x ** k * h1[i]) % m1

        n = len(t)
        h1, h2 = precomputehash(t)
        for i in range(0, n -k + 1):
            Htk = h1[i + k] % m1 - (x ** k * h1[i]) % m1
            if Htk in Hsk:
                print('gevonden op plekken: ', Hsk.index(Htk), i, k)
                found = True
                break  # no need to search further
        if found:
            break  # no need to check smaller k-values

    ans = solve(s, t)
    print(ans.i, ans.j, ans.len)

    # for line in sys.stdin.readlines():
    #     s, t = line.split()
    #     ans = solve(s, t)
    #     print(ans.i, ans.j, ans.len)
