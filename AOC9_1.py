lit = []
while True:
    x = input()
    if x == 'quit':
        break
    lit.append(x)

dx = {'R': 1, 'U': 0, 'D': 0, 'L': -1}
dy = {'R': 0, 'U': 1, 'D': -1, 'L': 0}
loc = set()
h = (0, 0)
t = (0, 0)
for i in lit:
    w, s = i.split()
    for j in range(int(s)):
        h = (h[0] + dx[w], h[1] + dy[w])
        dif_x = h[0] - t[0]
        dif_y = h[1] - t[1]
        if h[0] == t[0]:
            if dif_y == 2:
                t = (h[0], h[1] - 1)
            if dif_y == -2:
                t = (h[0], h[1] + 1)
        if h[1] == t[1]:
            if dif_x == 2:
                t = (h[0] - 1, h[1])
            if dif_x == -2:
                t = (h[0] + 1, h[1])
        if h[0] != t[0] and h[1] != t[1]:
            if abs(dif_x) == 2 and h[0] > t[0]:
                t = (h[0] - 1, h[1])
            if abs(dif_x) == 2 and h[0] < t[0]:
                t = (h[0] + 1, h[1])
            if abs(dif_y) == 2 and h[1] > t[1]:
                t = (h[0], h[1] - 1)
            if abs(dif_y) == 2 and h[1] < t[1]:
                t = (h[0], h[1] + 1)
        loc.add(t)

        print(h)
        print(t)
        print()
    print()

print(loc)
print(len(loc))
