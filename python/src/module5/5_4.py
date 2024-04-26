def preproc(arr):
    zero = [0] * (len(arr) + 1)
    for i in range(1, len(arr) + 1):
        zero[i] = zero[i - 1] + (arr[i - 1] == 0)
    return zero


def find_zero(zero, n, r, k):
    zeros_count = zero[r] - zero[n - 1]
    if zeros_count < k:
        return -1
    left, right = n, r
    while left < right:
        mid = (left + right) // 2
        if zero[mid] - zero[n - 1] >= k:
            right = mid
        else:
            left = mid + 1
    return left


N = int(input())
arr = list(map(int, input().split()))
Q = int(input())
zero = preproc(arr)
results = []
for _ in range(Q):
    n, r, k = map(int, input().split())
    result = find_zero(zero, n, r, k)
    results.append(result)

print(*results)
