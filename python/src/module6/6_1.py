class MaxElem:
    def __init__(self, max_size):
        self.heap = [0] * (max_size + 1)
        self.size = 0

    def shift_up(self, i):
        while i > 1 and self.heap[i] > self.heap[i // 2]:
            self.heap[i // 2], self.heap[i] = self.heap[i], self.heap[i // 2]
            i = i // 2
        return i

    def shift_down(self, i):
        while 2 * i <= self.size:
            left = 2 * i
            right = 2 * i + 1
            j = left
            if right <= self.size and self.heap[right] > self.heap[left]:
                j = right
            if self.heap[i] >= self.heap[j]:
                break
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i = j
        return i

    def insert(self, value):
        if self.size >= len(self.heap) - 1:
            return -1
        self.size += 1
        self.heap[self.size] = value
        return self.shift_up(self.size)

    def extract_max(self):
        if self.size == 0:
            return -1
        max_value = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        if self.size > 0:
            new_index = self.shift_down(1)
            return (new_index, max_value)
        return (0, max_value)


def print_elems(N, queries):
    pq = MaxElem(N)
    for query in queries:
        if query[0] == 1:
            if pq.size == 0:
                print(-1)
            else:
                result = pq.extract_max()
                print(result[0], result[1])
        elif query[0] == 2:
            result = pq.insert(query[1])
            print(result)

    print(' '.join(map(str, pq.heap[1:pq.size + 1])))


N, M = map(int, input().split())
queries = [list(map(int, input().split())) for _ in range(M)]
print_elems(N, queries)
