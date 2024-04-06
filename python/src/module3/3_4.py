def min_len(s):
    n = len(s)
    q = [0] * n
    k = 0
    res = 0

    for i in range(1, n):
        while k > 0 and s[i] != s[k]:
            k = q[k-1]
        if s[i] == s[k]:
            k += 1
        q[i] = k

    if q[n-1] > 0:
        res = n - q[n-1]
    else:
        res = n

    return res


s = input()
print(min_len(s))
