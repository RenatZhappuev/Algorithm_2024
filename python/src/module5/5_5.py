def divisor(a, b):
    while b:
        a, b = b, a % b
    return a


def build_tree(array, tree, node, start, end):
    if start == end:
        tree[node] = array[start]
    else:
        mid = (start + end) // 2
        build_tree(array, tree, 2 * node + 1, start, mid)
        build_tree(array, tree, 2 * node + 2, mid + 1, end)
        tree[node] = divisor(tree[2 * node + 1], tree[2 * node + 2])


def update_tree(array, tree, node, start, end, index, value):
    if start == end:
        array[index] = value
        tree[node] = value
    else:
        mid = (start + end) // 2
        if start <= index <= mid:
            update_tree(array, tree, 2 * node + 1, start, mid, index, value)
        else:
            update_tree(array, tree, 2 * node + 2, mid + 1, end, index, value)
        tree[node] = divisor(tree[2 * node + 1], tree[2 * node + 2])


def query_gcd(tree, node, start, end, n, r):
    if r < start or end < n:
        return 0
    if n <= start and end <= r:
        return tree[node]
    mid = (start + end) // 2
    left_gcd = query_gcd(tree, 2 * node + 1, start, mid, n, r)
    right_gcd = query_gcd(tree, 2 * node + 2, mid + 1, end, n, r)
    return divisor(left_gcd, right_gcd)


N = int(input().strip())
array = list(map(int, input().strip().split()))
Q = int(input().strip())
segment_tree_size = 2 * (2 ** (N - 1).bit_length()) - 1
tree = [0] * segment_tree_size
build_tree(array, tree, 0, 0, N - 1)
for _ in range(Q):
    query = input().strip().split()
    if query[0] == 's':
        n, r = int(query[1]) - 1, int(query[2]) - 1
        print(query_gcd(tree, 0, 0, N - 1, n, r))
    elif query[0] == 'u':
        i, v = int(query[1]) - 1, int(query[2])
        update_tree(array, tree, 0, 0, N - 1, i, v)
