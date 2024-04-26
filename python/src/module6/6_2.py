class MaxElem:
    def __init__(self, max_size):
        self.heap = [0] * (max_size + 1)
        self.size = 0
        self.index_map = {}

    def shift_up(self, i):
        while i > 1 and self.heap[i // 2] < self.heap[i]:
            self.index_map[self.heap[i]], \
                self.index_map[self.heap[i // 2]] = self.index_map[self.heap[i // 2]], self.index_map[self.heap[i]]
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
            self.index_map[self.heap[i]], \
                self.index_map[self.heap[j]] = self.index_map[self.heap[j]], self.index_map[self.heap[i]]
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i = j
        return i

    def insert(self, value):
        if self.size >= len(self.heap) - 1:
            return -1
        self.size += 1
        self.heap[self.size] = value
        self.index_map[value] = self.size
        return self.shift_up(self.size)

    def extract_max(self):
        if self.size == 0:
            return -1
        max_value = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.index_map[self.heap[1]] = 1
        self.size -= 1
        if self.size > 0:
            new_index = self.shift_down(1)
            return (new_index, max_value)
        return (0, max_value)

    def remove_by_index(self, index):
        if index < 1 or index > self.size:
            return -1
        value = self.heap[index]
        self.heap[index] = self.heap[self.size]
        self.index_map[self.heap[index]] = index
        self.size -= 1
        if self.size > 0:
            self.shift_down(index)
            self.shift_up(index)
        return value


def process_queries(N, queries):
    pq = MaxElem(N)
    for query in queries:
        if query[0] == 1:
            result = pq.extract_max()
            if result == -1:
                print(-1)
            else:
                print(result[0], result[1])
        elif query[0] == 2:
            result = pq.insert(query[1])
            print(result)
        elif query[0] == 3:
            result = pq.remove_by_index(query[1])
            if result == -1:
                print(-1)
            else:
                print(result)

    print(' '.join(map(str, pq.heap[1:pq.size + 1])))


N, M = map(int, input().split())
queries = [list(map(int, input().split())) for _ in range(M)]

process_queries(N, queries)
