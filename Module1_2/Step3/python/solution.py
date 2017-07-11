class Buffer:
    def __init__(self, max_size):
        self._buffer = []
        self._log = []
        self._max_size = max_size
        self._current_size = 0
        self._processing = 0

    def __repr__(self):
        return self._log

    def __str__(self):
        return "\n".join(map(str, self._log))

    def _push(self, arrival, duration):
        time = max(arrival, self._buffer[-1] if self._current_size else self._processing)
        self._log.append(time)
        self._buffer.append(time + duration)

    def append(self, arrival, duration):
        while (
            self._current_size and
            arrival >= self._buffer[0]
        ):
            self._processing = self._buffer.pop(0)
            self._current_size -= 1

        if self._current_size < self._max_size:
            self._push(arrival, duration)
            self._current_size += 1
        else:
            self._log.append(-1)


size, n = map(int, input().split())

buffer = Buffer(size)
for i in range(n):
    arrival, duration = map(int, input().split())
    buffer.append(arrival, duration)

print(buffer)
