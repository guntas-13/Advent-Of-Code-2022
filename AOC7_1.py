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
            for j in range(len(directs) + 1):
                dic['->'.join(directs[:j])] += size
        except:
            pass
print(dic)
print(directs)
sm = 0
for i in dic:
    t = dic[i]
    if t <= 100000:
        sm += t
print(sm)
