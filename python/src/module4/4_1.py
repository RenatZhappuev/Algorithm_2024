def stack(s):
    st = []
    c = 0
    for i in s:
        if i == '(':
            st.append(i)
        else:
            if len(st) == 0:
                c += 1
                print(st)
            else:
                st.pop()
    return c + len(st)


s = input()
print(stack(s))
