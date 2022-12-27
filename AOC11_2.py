lit = []
while True:
    x = input().strip()
    if x == 'quit':
        break
    lit.append(x)
items = {}
op = {}
test = {}
tr = {}
fl = {}
item = 0
for i in lit:
    t = i.split()
    if i == '':
        item += 1
    elif t[0] == 'Monkey':
        op[item] = ''
        test[item] = ''
        tr[item] = ''
        fl[item] = ''
    elif t[0] == 'Starting':
        x = i.split(', ')
        n = x.pop(0)
        x.insert(0, n[16] + n[17])
        items[item] = x
    elif t[0] == 'Operation:':
        op[item] += t[4] + t[5]
    elif t[0] == 'Test:':
        test[item] += t[3]
    elif t[1] == 'true:':
        tr[item] += t[5]
    elif t[1] == 'false:':
        fl[item] += t[5]
size = 8
for p in range(size):
    items[p] = list(map(int, items[p]))
    test[p] = int(test[p])
    tr[p] = int(tr[p])
    fl[p] = int(fl[p])

print(items)
print(op)
print(test)
print(tr)
print(fl)
print()

count = [0, 0, 0, 0, 0, 0, 0, 0]
ans = 7 * 11 * 13 * 3 * 17 * 2 * 5 * 19
# ans = 23 * 19 * 13 * 17
# count = [0, 0, 0, 0]
for k in range(10000):
    if k == 1 or k == 20 or k % 1000 == 0:
        print(count)
    for j in range(size):
        it = items[j].copy()
        if it != list():
            for x in it:
                count[j] += 1
                old = x
                cpy = old
                if op[j][0] == '*' and op[j] != '*old':
                    cpy *= int(op[j][1:])
                    new = cpy % ans
                elif op[j][0] == '+':
                    cpy += int(op[j][1:])
                    new = cpy % ans
                elif op[j] == '*old':
                    cpy = old ** 2
                    new = cpy % ans
                if new % test[j] == 0:
                    items[tr[j]].append(new)
                else:
                    items[fl[j]].append(new)
                items[j].pop(0)

print(count)
x1 = max(count)
count.remove(max(count))
x2 = max(count)
print(x1 * x2)
