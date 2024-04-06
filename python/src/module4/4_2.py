def st(s):
    stack = []
    curr = 1
    for i in s:
        stack.append(i)
        if i > stack[-1]:
            print('NO')
            break
        if i == curr:
            stack.pop()
            curr += 1
        while stack and stack[-1] == curr:
            curr += 1
            stack.pop()
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')


n = input()
s = list(map(int, input().split()))
st(s)
