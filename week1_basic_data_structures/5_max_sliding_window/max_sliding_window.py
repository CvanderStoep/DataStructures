# python3
from QueueWith2Stacks import Queue


def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums


def max_sliding_window(sequence, m):
    maximums = []
    n = len(sequence)
    # initial window
    window_sequence = sequence[0:m]
    q = Queue()
    for j in window_sequence:
        q.enQueue(j)
    maximums.append(q.Max())
    # sliding window
    for i in range(m, n):
        q.deQueue()
        q.enQueue(sequence[i])
        maximums.append(q.Max())
    return maximums


if __name__ == '__main__':
    # sample input:
    # 8
    # 2 7 3 1 5 2 6 2
    # 4
    # sample output:
    # 7 7 5 6 6
    n = int(input("input: \n"))
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    #optimized using Queue implemented with 2 stacks
    print(*max_sliding_window(input_sequence, window_size))

    #naive algorithm
    print(*max_sliding_window_naive(input_sequence, window_size))
