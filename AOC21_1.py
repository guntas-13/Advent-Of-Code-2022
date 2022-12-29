lit = []
while True:
    x = input()
    if x == 'quit':
        break
    lit.append(x.strip().split(":"))

dic = {}


def f(t, v):
    w = dic[t]
    if t == 'humn' and v >= 0:
        return v
    try:
        return int(w[0])
    except:
        a, b = f(w[0], v), f(w[2], v)
        if w[1] == '+':
            dic[t] = [str(int(a + b))]
            return a + b
        if w[1] == '-':
            dic[t] = [str(int(a - b))]
            return a - b
        if w[1] == '*':
            dic[t] = [str(int(a * b))]
            return a * b
        if w[1] == '/':
            dic[t] = [str(int(a / b))]
            return a / b


for x in lit:
    dic[x[0]] = x[1].split()

n1, n2 = dic['root'][0], dic['root'][2]
print(int(f(n1, 0)), int(f(n2, 0)))
print(dic)

'''count = 308 * (10 ** 10)
while dic[n1] != dic[n2]:
    for x in lit:
        dic[x[0]] = x[1].split()
    dic['humn'] = [str(count)]
    f('root')
    if count % (10 ** 11) == 0 or count % (10 ** 10) == 0 or count % (10 ** 9) == 0 or count % (
            10 ** 8) == 0 or count % (10 ** 7) == 0 or count % (10 ** 6) == 0 or count % (10 ** 5) == 0 or count % (
            10 ** 4) == 0:
        print(count)
    count += 1
print(count - 1) 

'''
target = f(n2, 0)

lo = 0
hi = int(1e20)
while lo < hi:
    mid = (lo + hi) // 2
    score = target - f(n1, mid)
    if score < 0:
        lo = mid
    elif score == 0:
        print(mid)
        break
    else:
        hi = mid
