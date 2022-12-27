lit = []
while True:
    x = input()
    lit.append(x)
    if x == 'quit':
        break
count = 0
for i in lit[:-1]:
    t = i.split(",")
    x1 = t[0].split("-")
    x2 = t[1].split("-")
    s1 = set(list(range(int(x1[0]), int(x1[1]) + 1)))
    s2 = set(list(range(int(x2[0]), int(x2[1]) + 1)))
    if len(s1 & s2) > 0:
        count += 1
print(count)
