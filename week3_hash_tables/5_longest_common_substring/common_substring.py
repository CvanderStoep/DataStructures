# python3

import sys
from collections import namedtuple
from substring_equality import precomputehash

Answer = namedtuple('answer_type', 'i j len')


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
    hs1, hs2, m1, m2, x = precomputehash(s)
    ht1, ht2, _, _, _ = precomputehash(t)

    found = False
    for k in range(min(len(s), len(t)), 0, -1):
        n = len(s)
        Hsk = [0] * (n - k + 1)
        for i in range(0, n - k + 1):
            Hsk[i] = (hs1[i + k] % m1 - (x ** k * hs1[i]) % m1) % m1

        n = len(t)
        for i in range(0, n - k + 1):
            Htk = (ht1[i + k] % m1 - (x ** k * ht1[i]) % m1) % m1
            if Htk in Hsk:
                print('gevonden op plekken: ', Hsk.index(Htk), i, k)
                print(t[i:i + k])
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
