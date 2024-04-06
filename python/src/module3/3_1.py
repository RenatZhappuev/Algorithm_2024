def get_hash(string, length, x, pr):
    hash_val = 0
    for i in range(length):
        hash_val = (hash_val * x + ord(string[i])) % pr
    return hash_val


def rabin_karp(s: str, t: str):
    pr = 10**9+8
    x = 26
    n = len(s)
    m = len(t)
    ht = get_hash(t, m, x, pr)
    hs = get_hash(s, m, x, pr)
    if n <= m:
        return []

    xt = 1
    for i in range(m - 1):
        xt = (xt * x) % pr

    res = []
    for i in range(n - m + 1):
        if hs == ht and s[i:i + m] == t:
            res.append(i)
        if i < n - m:
            hs = (hs - ord(s[i]) * xt) % pr
            hs = (hs * x + ord(s[i + m])) % pr
            if hs < 0:
                hs += pr
    return res


S = input()
T = input()
res = rabin_karp(S, T)
if len(res) == 0:
    print(-1)
else:
    print(*res)
