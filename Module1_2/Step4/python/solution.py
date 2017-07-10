class Stack:
    def __init__(self):
        super(Stack, self).__init__()
        self._list = []
        self._max_list = []

    def push(self, value):
        """
        S.push(value) -- push value to the end of the sequence.
        """
        self._list.append(value)
        self._max_list.append(max(value, self._max_list[-1]) if self._max_list else value)

    def pop(self, index=-1):
        """
        S.pop([index]) -> item -- remove and return item at index (default last).
        Raise IndexError if list is empty or index is out of range.
        """
        v = self._list[index]
        del self._list[index]
        del self._max_list[index]
        return v

    def max(self):
        """
        S.max() -> item -- return item with max value.
        Raise ValueError if list is empty.
        """
        return self._max_list[-1]


n = int(input())

stack = Stack()
for i in range(n):
    command = input().split()
    if command[0] == "max":
        print(stack.max())
    elif command[0] == "pop":
        stack.pop()
    else:
        stack.push(int(command[1]))
