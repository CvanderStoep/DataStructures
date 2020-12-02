class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__maxstack = []  # keep an auxiliary stack containing running maxima

    def Push(self, a):
        # push element to the stack and update auxiliary stack if needed
        self.__stack.append(a)

        # if maxstack is empty (first element) or new element > maximum, add to the maxstack
        if len(self.__maxstack) == 0:
            self.__maxstack.append(a)
        elif a >= self.Max():
            self.__maxstack.append(a)

    def Pop(self):
        # if the maximum is removed from the stack, remove it also from auxiliary stack.
        if len(self.__stack) == 0:
            print('stack contains no elements')
            return
        # assert (len(self.__stack))
        if self.__stack[-1] == self.__maxstack[-1]:
            self.__maxstack.pop()
        return self.__stack.pop()

    def Max(self):
        if len(self.__maxstack) == 0: return None
        # assert len(self.__maxstack), 'contains no elements'
        return self.__maxstack[-1]

    def Size(self):
        return len(self.__stack)

    def Is_empty(self):
        return self.Size() == 0
