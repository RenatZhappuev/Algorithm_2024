def build_tree(array, tree, node, start, end):
    if start == end:
        tree[node] = 1 if array[start] == 0 else 0
    else:
        mid = (start + end) // 2
        build_tree(array, tree, 2 * node + 1, start, mid)
        build_tree(array, tree, 2 * node + 2, mid + 1, end)
        tree[node] = (tree[2 * node + 1] + tree[2 * node + 2])


def update_tree(array, tree, node, start, end, index, value):
    if start == end:
        array[index] = value
        tree[node] = 1 if value == 0 else 0
    else:
        mid = (start + end) // 2
        if start <= index <= mid:
            update_tree(array, tree, 2 * node + 1, start, mid, index, value)
        else:
            update_tree(array, tree, 2 * node + 2, mid + 1, end, index, value)
        tree[node] = (tree[2 * node + 1] + tree[2 * node + 2])


def zero_count(tree, node, start, end, n, r):
    if r < start or end < n:
        return 0
    if n <= start and end <= r:
        return tree[node]
    mid = (start + end) // 2
    left_count = zero_count(tree, 2 * node + 1, start, mid, n, r)
    right_count = zero_count(tree, 2 * node + 2, mid + 1, end, n, r)
    return left_count + right_count


def find_zero(tree, array, node, start, end, n, r, k):
    if k > zero_count(tree, node, start, end, n, r):
        return -1
    if start == end:
        return start
    mid = (start + end) // 2
    left_zero_count = zero_count(tree, 2 * node + 1, start, mid, n, r)
    if left_zero_count >= k:
        return find_zero(tree, array, 2 * node + 1, start, mid, n, r, k)
    else:
        return find_zero(tree, array, 2 * node + 2, mid + 1, end, n, r, k - left_zero_count)


N = int(input().strip())
array = list(map(int, input().strip().split()))
Q = int(input().strip())

segment_tree_size = 2 * (2 ** (N - 1).bit_length()) - 1
tree = [0] * segment_tree_size

build_tree(array, tree, 0, 0, N - 1)

for _ in range(Q):
    query = input().strip().split()
    if query[0] == 's':
        n, r, k = int(query[1]) - 1, int(query[2]) - 1, int(query[3])
        zero_c = zero_count(tree, 0, 0, N - 1, n, r)
        if k > zero_c:
            print(-1)
        else:
            zero_index = find_zero(tree, array, 0, 0, N - 1, n, r, k)
            print(zero_index + 1 if zero_index != -1 else -1)
    elif query[0] == 'u':
        i, v = int(query[1]) - 1, int(query[2])
        update_tree(array, tree, 0, 0, N - 1, i, v)
