lit = []
while True:
    x = input()
    if x == 'quit':
        break
    a, b, c = x.split(",")
    a, b, c = int(a), int(b), int(c)
    lit.append((a, b, c))
size = len(lit)
area = size * 6
for i in range(size):
    for j in range(i + 1, size):
        prev = lit[i]
        new = lit[j]
        dx = abs(prev[0] - new[0])
        dy = abs(prev[1] - new[1])
        dz = abs(prev[2] - new[2])
        if (prev[0] == new[0] and prev[1] == new[1] and dz == 1) or (
                prev[0] == new[0] and prev[2] == new[2] and dy == 1) or (
                prev[2] == new[2] and prev[1] == new[1] and dx == 1):
            area -= 2
print(area)
