lit = [['D', 'H', 'R', 'Z', 'S', 'P', 'W', 'Q'], ['F', 'H', 'Q', 'W', 'R', 'B', 'V'], ['H', 'S', 'V', 'C'],
       ['G', 'F', 'H'], ['Z', 'B', 'J', 'G', 'P'], ['L', 'F', 'W', 'H', 'J', 'T', 'Q'],
       ['N', 'J', 'V', 'L', 'D', 'W', 'T', 'Z'], ['F', 'H', 'G', 'J', 'C', 'Z', 'T', 'D'],
       ['H', 'B', 'M', 'V', 'P', 'W']]
num = []
initial = []
final = []
while True:
    x = input()
    if x == 'quit':
        break
    t = x.split()
    num.append(int(t[1]))
    initial.append(int(t[3]))
    final.append(int(t[5]))

for i in range(len(num)):
    n = num[i]
    while n > 0:
        lit[final[i] - 1].insert(0, (lit[initial[i] - 1][0]))
        lit[initial[i] - 1].pop(0)
        n -= 1
for j in range(9):
    print(lit[j][0], end="")
