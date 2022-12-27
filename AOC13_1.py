def func(a, b):
    if type(a) == int and type(b) == int:
        if a < b:
            return 1
        elif a == b:
            return 2
        else:
            return 3
    elif type(a) == list and type(b) == int:
        return func(a, [b])
    elif type(b) == list and type(a) == int:
        return func([a], b)
    elif type(a) == list and type(b) == list:
        i = 0
        while i < len(a) and i < len(b):
            res = func(a[i], b[i])
            if res == 1:
                return 1
            if res == 3:
                return 3
            i += 1
        if i == len(a) and i < len(b):
            return 1
        elif i == len(b) and i < len(a):
            return 3
        else:
            return 2


lit = []
st = ""
while True:
    x = input()
    if x == "":
        lit.append(st.split())
        st = ""
        continue
    st += x + " "
    if x == 'quit':
        break
count = 0
index = 1
print(lit)
for x in lit:
    l1 = eval(x[0])
    l2 = eval(x[1])
    print(l1, l2)
    fin = func(l1, l2)
    print(fin)
    print()
    if fin == 1:
        count += index
    index += 1
print()
print(count)
