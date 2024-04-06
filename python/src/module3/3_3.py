def z_func(s: str) -> list:
    n = len(s)
    z = [0]*n
    left = 0
    right = 0
    for i in range(1, n):
        if (i <= right):
            z[i] = min(right - i + 1, z[i - left])
        while (i + z[i] < n) and (s[z[i]] == s[i+z[i]]):
            z[i] += 1
        if (i + z[i] - 1 > right):
            left = i
            right = i + z[i] - 1
    return z


s = input()
q = z_func(s)
n = len(s)
flag = False
for i, x in enumerate(q):
    if (i + x == n) and (n % i == 0):
        print(n//i)
        flag = True
        break
if not flag:
    print(1)
