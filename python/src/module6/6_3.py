class PyramidSort:
    def __init__(self, heap):
        self.heap = heap
        self.size = len(heap)
        self.build_heap()

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def shift_up(self, i):
        while i > 0 and self.heap[i] > self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def shift_down(self, i):
        max_index = i
        left = self.left_child(i)
        if left < self.size and self.heap[left] > self.heap[max_index]:
            max_index = left
        right = self.right_child(i)
        if right < self.size and self.heap[right] > self.heap[max_index]:
            max_index = right
        if i != max_index:
            self.heap[i], self.heap[max_index] = self.heap[max_index], self.heap[i]
            self.shift_down(max_index)

    def build_heap(self):
        for i in range(self.size // 2, -1, -1):
            self.shift_down(i)

    def pop(self):
        max_value = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.heap.pop()
        self.shift_down(0)
        return max_value


def heap_sort(heap):
    max_heap = PyramidSort(heap)
    sorted_array = []
    print(' '.join(map(str, max_heap.heap)))  # Вывод построенной кучи
    while max_heap.size > 0:
        max_value = max_heap.pop()
        sorted_array.append(max_value)
        if max_heap.size > 0:
            print(' '.join(map(str, max_heap.heap[:max_heap.size])))
    return sorted_array


n = int(input())
data = list(map(int, input().split()))
sorted_array = heap_sort(data)
sorted_array = sorted_array[::-1]
print(' '.join(map(str, sorted_array)))
