# python3
import StackWithMax
import QueueWith2Stacks



def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

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

    # initial window
    window_sequence = input_sequence[0:window_size]
    q = QueueWith2Stacks.Queue()
    for j in window_sequence:
        q.enQueue(j)
    print(q.Max(), end= " ")
    # sliding window
    for i in range(window_size, n):
        q.deQueue()
        q.enQueue(input_sequence[i])
        print(q.Max(), end = " ")
    print()


    print(*max_sliding_window_naive(input_sequence, window_size))
