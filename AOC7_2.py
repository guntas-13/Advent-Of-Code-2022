from collections import defaultdict

lit = []
while True:
    x = input()
    if x == 'quit':
        break
    lit.append(x)
directs = []
dic = defaultdict(int)
for i in lit:
    line = i.split()
    if line[1] == 'cd':
        if line[2] == '..':
            directs.pop()
        else:
            directs.append(line[2])
    elif line[1] == 'ls':
        continue
    else:
        try:
            size = int(line[0])
            print(directs, size)
            for j in range(1, len(directs) + 1):
                dic['->'.join(directs[:j])] += size
        except:
            pass
print(dic)
print(directs)
val = 40000000
old = dic['/']
diff = old - val
fin = []
for i in dic:
    t = dic[i]
    if t >= diff:
        fin.append(t)
print(min(fin))
