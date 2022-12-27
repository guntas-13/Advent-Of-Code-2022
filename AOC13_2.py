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
while True:
    x = input()
    if x=="":
        continue
    if x == 'quit':
        break
    lit.append(x)
lit.extend(["[[2]]","[[6]]"])

fin=[]
for x in lit:
    l=[]
    for t in lit:
        l.append(func(eval(x),eval(t)))
    fin.append(l.count(3))
x1=fin[-2]+1
x2=fin[-1]+1
print(x1,x2,x1*x2)
