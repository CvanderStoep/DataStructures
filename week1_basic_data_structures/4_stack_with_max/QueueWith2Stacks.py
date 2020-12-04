from StackWithMax import StackWithMax


class Queue:
    def __init__(self):
        self.s1 = StackWithMax()
        self.s2 = StackWithMax()

    # EnQueue item to the queue
    def enQueue(self, x):
        self.s1.Push(x)

    # DeQueue item from the queue
    def deQueue(self):

        # if both the stacks are empty
        if self.s1.Is_empty() and self.s2.Is_empty():
            print("Q is Empty")
            return

        # if s2 is empty and s1 has elements
        elif self.s2.Is_empty() and not self.s1.Is_empty():
            while not self.s1.Is_empty():
                temp = self.s1.Pop()
                self.s2.Push(temp)
            return self.s2.Pop()

        else:
            return self.s2.Pop()

    def Max(self):
        if self.s1.Max() is None and self.s2.Max() is None: return
        if self.s1.Max() is None and self.s2.Max() is not None: return self.s2.Max()
        if self.s1.Max() is not None and self.s2.Max() is None: return self.s1.Max()
        return max(self.s1.Max(), self.s2.Max())


if __name__ == '__main__':
    q = Queue()
    q.enQueue(5)
    q.enQueue(2)
    q.enQueue(4)
    print("max: ", q.Max())
    print(q.deQueue())
    print("max: ", q.Max())
    print(q.deQueue())
    q.enQueue(8)
    print("max: ", q.Max())
    print(q.deQueue())
    print(q.deQueue())
    print("max: ", q.Max())
