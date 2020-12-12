import sys

class Max_Heap_index1_based:
    # index 1 based
    def __init__(self):
        self.array = ['dummy']  # dummy element to use an array starting at index 1
        # self.size = len(self.array)

    # return the node number of the Parent
    def Parent(self, i):
        return i // 2

    def Size(self):
        return len(self.array) - 1

    # return the node number of the left child
    def LeftChild(self, i):
        return 2 * i

    # return the node number of the right child
    def RightChild(self, i):
        return 2 * i + 1

    def SiftUp(self, i):
        while i > 1 and self.array[self.Parent(i)] < self.array[i]:
            self.array[self.Parent(i)], self.array[i] = self.array[i], self.array[self.Parent(i)]
            i = self.Parent(i)

    def SiftDown(self, i):
        maxIndex = i
        l = self.LeftChild(i)
        if l <= self.Size() and self.array[l] > self.array[maxIndex]:
            maxIndex = l
        r = self.RightChild(i)
        if r <= self.Size() and self.array[r] > self.array[maxIndex]:
            maxIndex = r
        if i != maxIndex:
            self.array[i], self.array[maxIndex] = self.array[maxIndex], self.array[i]
            self.SiftDown(maxIndex)

    def Insert(self, p):
        self.array.append(p)
        self.SiftUp(self.Size())

    def ExtractMax(self):
        result = self.array[1]
        self.array[1] = self.array[self.Size()]
        self.array.pop()
        self.SiftDown(1)
        return result

    def Remove(self, i):
        self.array[i] = sys.maxsize
        self.SiftUp(i)
        self.ExtractMax()

    def ChangePriority(self, i, p):
        oldp = self.array[i]
        self.array[i] = p
        if p > oldp:
            self.SiftUp(i)
        else:
            self.SiftDown(i)

    def BuildHeap(self, new_array):
        self.array += new_array
        for i in range(self.Size() // 2, 0, -1):
            self.SiftDown(i)


class Max_Heap:
    """"This class implements the maxHeap Data structure."""

    # index 0 based
    def __init__(self):
        self.array = []
        self.size = 0

    # return the node number of the Parent
    def Parent(self, i):
        return (i - 1) // 2

    # return the node number of the left child
    def LeftChild(self, i):
        return 2 * i + 1

    # return the node number of the right child
    def RightChild(self, i):
        return 2 * i + 2

    def SiftUp(self, i):
        while i > 0 and self.array[self.Parent(i)] < self.array[i]:
            self.array[self.Parent(i)], self.array[i] = self.array[i], self.array[self.Parent(i)]
            i = self.Parent(i)

    def SiftDown(self, i):
        maxIndex = i
        l = self.LeftChild(i)
        if l <= self.size - 1 and self.array[l] > self.array[maxIndex]:
            maxIndex = l
        r = self.RightChild(i)
        if r <= self.size - 1 and self.array[r] > self.array[maxIndex]:
            maxIndex = r
        if i != maxIndex:
            self.array[i], self.array[maxIndex] = self.array[maxIndex], self.array[i]
            self.SiftDown(maxIndex)

    def Insert(self, p):
        self.size += 1
        self.array.append(p)
        self.SiftUp(self.size - 1)

    def ExtractMax(self):
        result = self.array[0]
        self.array[0] = self.array[self.size - 1]
        self.size -= 1
        self.array.pop()
        self.SiftDown(0)
        return result

    def Remove(self, i):
        self.array[i] = sys.maxsize
        self.SiftUp(i)
        self.ExtractMax()

    def ChangePriority(self, i, p):
        oldp = self.array[i]
        self.array[i] = p
        if p > oldp:
            self.SiftUp(i)
        else:
            self.SiftDown(i)

    def BuildHeap(self, new_array):
        self.array += new_array
        self.size = len(self.array)
        # starting at the second-last row for SiftDown
        for i in range((self.size + 1) // 2 - 1, -1, -1):  # [n/2] ... 1 (when starting at index 1)
            self.SiftDown(i)


# DONE transform maxheap into minheap
class Min_Heap:
    # index 0 based
    def __init__(self):
        self.array = []
        self.size = 0
        self.swaps = []

    # return the node number of the Parent
    def Parent(self, i):
        return (i - 1) // 2

    # return the node number of the left child
    def LeftChild(self, i):
        return 2 * i + 1

    # return the node number of the right child
    def RightChild(self, i):
        return 2 * i + 2

    def SiftUp(self, i):
        while i > 0 and self.array[self.Parent(i)] > self.array[i]:
            self.array[self.Parent(i)], self.array[i] = self.array[i], self.array[self.Parent(i)]
            i = self.Parent(i)

    def SiftDown(self, i):
        maxIndex = i
        l = self.LeftChild(i)
        if l <= self.size - 1 and self.array[l] < self.array[maxIndex]:
            maxIndex = l
        r = self.RightChild(i)
        if r <= self.size - 1 and self.array[r] < self.array[maxIndex]:
            maxIndex = r
        if i != maxIndex:
            # print('swap: ', i, maxIndex)
            self.swaps.append((i, maxIndex))
            self.array[i], self.array[maxIndex] = self.array[maxIndex], self.array[i]
            self.SiftDown(maxIndex)
        # return self.swaps

    def Insert(self, p):
        self.size += 1
        self.array.append(p)
        self.SiftUp(self.size - 1)

    def ExtractMin(self):
        result = self.array[0]
        self.array[0] = self.array[self.size - 1]
        self.size -= 1
        self.array.pop()
        self.SiftDown(0)
        return result

    def Remove(self, i):
        self.array[i] = - sys.maxsize
        self.SiftUp(i)
        self.ExtractMin()

    def ChangePriority(self, i, p):
        oldp = self.array[i]
        self.array[i] = p
        if p < oldp:
            self.SiftUp(i)
        else:
            self.SiftDown(i)

    def BuildHeap(self, new_array):
        self.array += new_array
        self.size = len(self.array)
        # starting at the second-last row for SiftDown
        for i in range((self.size + 1) // 2 - 1, -1, -1):  # [n/2] ... 1 (when starting at index 1)
            self.SiftDown(i)
        return self.swaps


def main():
    print('building first maxHeap ...')
    maxH = Max_Heap()
    maxH.Insert(3)
    maxH.Insert(29)
    maxH.Insert(18)
    maxH.Insert(14)
    maxH.Insert(7)
    maxH.Insert(18)
    maxH.Insert(12)
    maxH.Insert(11)
    maxH.Insert(13)
    print(maxH.array)

    print('building second maxHeap ...')
    maxH2 = Max_Heap()
    maxH2.BuildHeap([3, 29, 40, 14, 7, 18, 49, 11, 57])
    print(maxH2.array)
    maxH2.ChangePriority(0, 1)
    print(maxH2.array)

    print('building third maxHeap ...')
    maxH3 = Max_Heap()
    array = []
    for i in range(10):
        array.append(i)
    maxH3.BuildHeap(array)
    print(maxH3.array)

    print('building first minHeap ...')
    minH1 = Min_Heap()
    minH1.BuildHeap([3, 29, 40, 14, 7, 18, 49, 11, 57])
    print(minH1.array)
    minH1.ChangePriority(0, 9)
    print(minH1.array)
    print(minH1.ExtractMin())
    print(minH1.array)

    print('building second minHeap ...')
    minHeap = Min_Heap()
    print('swaps: ', minHeap.BuildHeap([7, 8, 3, 1, 5, 4, 3, 2, 1]))
    print('heap: ', minHeap.array)

    print('building third minHeap with tuples...')
    minHeap = Min_Heap()
    print('swaps: ', minHeap.BuildHeap([(7, 1), (8, 5), (3, 7), (1, 4), (5, 6), (4, 10), (3, 7), (2, 1), (1, 5)]))
    print('heap: ', minHeap.array)


if __name__ == "__main__":
    main()
