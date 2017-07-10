class Stack:
    def __init__(self):
        super(Stack, self).__init__()
        self._list = []
        self._max_list = []

    def __bool__(self):
        return True if self._list else False

    def push(self, value):
        self._list.append(value)
        self._max_list.append(max(value, self._max_list[-1]) if self._max_list else value)

    def pop(self, index=-1):
        v = self._list[index]
        del self._list[index]
        del self._max_list[index]
        return v

    def max(self):
        return self._max_list[-1]


class Queue:
    def __init__(self):
        self.first = Stack()
        self.second = Stack()

    def push(self, value):
        self.first.push(value)

    def pop(self):
        if not self.second:
            while self.first:
                self.second.push(self.first.pop())
        return self.second.pop()

    def max(self):

        if not self.first:
            return self.second.max()

        if not self.second:
            return self.first.max()

        return max(self.first.max(), self.second.max())


def maxs_in_windows(lst, w):
    if w == 1:
        return lst

    result = []
    queue = Queue()

    for index, value in enumerate(lst, start=1):
        queue.push(value)

        if index >= w:
            result.append(queue.max())
            queue.pop()

    return result


n = int(input())
A = map(int, input().split())
m = int(input())

print(" ".join(map(str, maxs_in_windows(A, m))))
