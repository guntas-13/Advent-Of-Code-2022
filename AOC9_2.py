lit = []
while True:
    x = input()
    if x == 'quit':
        break
    lit.append(x)


def pos(h, t):
    dif_x = h[0] - t[0]
    dif_y = h[1] - t[1]
    if abs(dif_x) <= 1 and abs(dif_y) <= 1:
        pass
    elif abs(dif_x) >= 2 and abs(dif_y) >= 2:
        t = (h[0] - 1 if t[0] < h[0] else h[0] + 1, h[1] - 1 if t[1] < h[1] else h[1] + 1)
    elif abs(dif_x) >= 2:
        t = (h[0] - 1 if t[0] < h[0] else h[0] + 1, h[1])
    elif abs(dif_y) >= 2:
        t = (h[0], h[1] - 1 if t[1] < h[1] else h[1] + 1)
    return t


dx = {'R': 1, 'U': 0, 'D': 0, 'L': -1}
dy = {'R': 0, 'U': 1, 'D': -1, 'L': 0}
H = (0, 0)
T = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
loc = {T[8]}
for i in lit:
    w, s = i.split()
    for j in range(int(s)):
        H = (H[0] + dx[w], H[1] + dy[w])
        T[0] = pos(H, T[0])
        for k in range(1, 9):
            T[k] = pos(T[k - 1], T[k])
        loc.add(T[8])
print(H)
print(T)
print(loc)
print(len(loc))
