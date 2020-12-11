import sys


class Max_Heap:
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
        for i in range(self.Size()//2, 0, -1):
            self.SiftDown(i)

def main():
    maxH = Max_Heap()
    maxH.Insert(3)
    # print(maxH.array)
    maxH.Insert(29)
    # print(maxH.array)
    maxH.Insert(18)
    # print(maxH.array)
    maxH.Insert(14)
    # print(maxH.array)
    maxH.Insert(7)
    # print(maxH.array)
    maxH.Insert(18)
    # print(maxH.array)
    maxH.Insert(12)
    # print(maxH.array)
    maxH.Insert(11)
    # print(maxH.array)
    maxH.Insert(13)
    # print(maxH.array)
    # print(maxH.ExtractMax())
    print(maxH.array)

    maxH2 = Max_Heap()
    maxH2.BuildHeap([3, 29, 18, 14, 7, 18, 12, 11, 13])
    print(*maxH2.array)


if __name__ == "__main__":
    main()
