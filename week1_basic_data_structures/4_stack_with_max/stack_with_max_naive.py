# python3
import sys


class StackWithMaxNaive():
    def __init__(self):
        self.__stack = []

    def Push(self, a):
        self.__stack.append(a)

    def Pop(self):
        if len(self.__stack) == 0:
            print('stack contains no elements')
            return
        # assert (len(self.__stack))
        self.__stack.pop()

    def Max(self):
        if len(self.__stack) == 0: return 'stack contains no elements'
        # assert (len(self.__stack))
        return max(self.__stack)


class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__maxstack = []  # keep an auxiliary stack containing running maxima

    def Push(self, a):
        # push element to the stack and update auxiliary stack if needed
        self.__stack.append(a)

        # if maxstack is empty (first element) or new element > maximum, add to the maxstack
        if len(self.__maxstack) == 0 or a >= self.Max():
            self.__maxstack.append(a)

    def Pop(self):
        # if the maximum is removed from the stack, remove it also from auxiliary stack.
        if len(self.__stack) == 0:
            print('stack contains no elements')
            return
        # assert (len(self.__stack))
        if self.__stack[-1] == self.__maxstack[-1]:
            self.__maxstack.pop()
        self.__stack.pop()

    def Max(self):
        if len(self.__maxstack) == 0: return 'stack contains no elements'
        # assert len(self.__maxstack), 'contains no elements'
        return self.__maxstack[-1]


# TODO write stress-test with randomized input
# stacknaive and stack should give same output

if __name__ == '__main__':
    input_lines = ["push 2", "push 1", "max", "pop", "max", "pop", "pop", "push 8", "max"]
    n = len(input_lines)

    # stack = StackWithMaxNaive()
    stack = StackWithMax()

    for _ in range(n):
        q = input_lines.pop(0).split()

        if q[0] == "push":
            stack.Push(int(q[1]))
        elif q[0] == "pop":
            stack.Pop()
        elif q[0] == "max":
            print(stack.Max())
        else:
            assert 0

    # num_queries = int(sys.stdin.readline())
    # for _ in range(num_queries):
    #     query = sys.stdin.readline().split()
    #
    #     if query[0] == "push":
    #         stack.Push(int(query[1]))
    #     elif query[0] == "pop":
    #         stack.Pop()
    #     elif query[0] == "max":
    #         print(stack.Max())
    #     else:
    #         assert 0
