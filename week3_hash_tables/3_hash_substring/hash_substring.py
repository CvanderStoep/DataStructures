# python3

def PolyHash(S, x=263, prime=1000000007):
    # x = 263  # random number between 1 and p-1
    # prime = 1000000007  # big prime number
    # implemented without cardinality of the hash function
    hash = 0
    for c in reversed(S):
        hash = (hash * x + ord(c)) % prime
    return hash


def PreComputeHashes(T, lenP):
    x = 263  # random number between 1 and p-1
    prime = 1000000007  # big prime number

    H = [0] * (len(T) - lenP + 1)
    start = len(T) - lenP
    finish = len(T) - 1
    S = T[start: finish + 1]  # finish element to be included in the slice
    H[len(T) - lenP] = PolyHash(S, x=x)
    y = 1
    for i in range(1, lenP + 1):
        y = (y * x) % prime
    for i in range(len(T) - lenP - 1, -1, -1):  # end = 0
        H[i] = (x * H[i + 1] + ord(T[i]) - y * ord(T[i + lenP]))

        #  do not use modulo calculation with negative numbers!
        if H[i] < 0:
            H[i] += (abs(H[i]) // prime + 1) * prime
        H[i] = H[i] % prime
    return H


def RabinKarp(text, pattern):
    result = []
    #  implement slide 14 first and afterwords slide 23 and 25
    card = len(pattern)
    pHash = PolyHash(pattern)
    for i in range(len(text) - len(pattern) + 1):
        tHash = PolyHash(text[i:i + len(pattern)])
        if pHash != tHash:
            continue
        if text[i:i + len(pattern)] == pattern:
            result.append(i)
    return result


def RabinKarp_precompute(text, pattern):
    result = []
    #  implement slide 14 first and afterwords slide 23 and 25
    card = len(pattern)
    pHash = PolyHash(pattern)
    H = PreComputeHashes(text, lenP=card)
    for i in range(len(text) - len(pattern) + 1):
        if pHash != H[i]:
            continue
        if text[i:i + len(pattern)] == pattern:
            result.append(i)
    return result


def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    # naive implementation
    return [
        i
        for i in range(len(text) - len(pattern) + 1)
        if text[i:i + len(pattern)] == pattern
    ]


if __name__ == '__main__':
    Pattern, Text = read_input()
    print_occurrences(get_occurrences(pattern=Pattern, text=Text))
    print('RabinKarp: ', RabinKarp(pattern=Pattern, text=Text))
    print('RabinKarp2: ', RabinKarp_precompute(pattern=Pattern, text=Text))
