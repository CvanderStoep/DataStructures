# python3
import Heap
import os


def build_heap_naive(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # DONE: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n
    data2 = list(data)

    swaps = build_heap_naive(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)

    print('building minHeap . . .')
    minHeap = Heap.Min_Heap()
    swaps = minHeap.BuildHeap(data2)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)

    with open("output.txt", "w") as f:
        print(len(swaps), file=f)
        for i, j in swaps:
            print(i, j, file=f)


if __name__ == "__main__":
    main()
