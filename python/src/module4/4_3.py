def st(s: list) -> list:
    stack = []
    res = [-1]*len(s)

    for i in range(len(s)-1):
        for j in range(len(s)-1):
            # while len(stack) > 1 and s[i] > stack[-1]:
            #     stack.pop()
            #     ind += 1
            #     res[i] = ind
            # print(stack)
            while len(stack) > 1 and stack[-1] < s[i]:
                stack.pop()
        stack.append(s[i])
        print(stack)
    return stack



n = input()
s = list(map(int, input().split()))
print(st(s))
