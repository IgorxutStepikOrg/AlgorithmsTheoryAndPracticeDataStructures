from collections import deque


def maxs_in_windows(lst, w):
    result = []

    queue = deque()

    len_lst = len(lst)
    for i in range(len_lst):

        while (
            queue and
            lst[i] >= lst[queue[-1]]
        ):
            queue.pop()

        queue.append(i)

        if (
            i >= w and
            queue and
            queue[0] <= (i - w)
        ):
            queue.popleft()

        if i >= (w - 1):
            result.append(lst[queue[0]])

    return result


n = int(input())
A = list(map(int, input().split()))
m = int(input())

print(" ".join(map(str, maxs_in_windows(A, m))))
