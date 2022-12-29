lit = []
while True:
    x = input()
    if x == 'quit':
        break
    lit.append(x.strip().split(":"))

dic = {}


def f(t):
    w = dic[t]
    try:
        return int(w[0])
    except:
        a, b = f(w[0]), f(w[2])
        if w[1] == '+':
            dic[t] = a + b
            return a + b
        if w[1] == '-':
            dic[t] = a - b
            return a - b
        if w[1] == '*':
            dic[t] = a * b
            return a * b
        if w[1] == '/':
            dic[t] = a / b
            return a / b


for x in lit:
    dic[x[0]] = x[1].split()
print(f("root"))
