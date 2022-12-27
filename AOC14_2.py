lines = []
while True:
    x = input()
    if x == 'quit':
        break
    h = []
    for k in x.split():
        if k != '->':
            h.append(k)
    lines.append(h)
pos = set()
for x in lines:
    old_pos = None
    for t in x:
        x, y = t.split(",")
        new_pos = (int(x), int(y))
        if old_pos is not None:
            dx = new_pos[0] - old_pos[0]
            dy = new_pos[1] - old_pos[1]
            for i in range(max(abs(dx), abs(dy)) + 1):
                x1 = old_pos[0] + i * (1 if dx > 0 else (-1 if dx < 0 else 0))
                y1 = old_pos[1] + i * (1 if dy > 0 else (-1 if dy < 0 else 0))
                pos.add((x1, y1))
        old_pos = new_pos
print(pos)
print(len(pos))
floor = 2 + max(r[1] for r in pos)
print(floor)
lo_x = min(r[0] for r in pos) - 2000
hi_x = max(r[0] for r in pos) + 2000
for x in range(lo_x, hi_x):
    pos.add((x, floor))
print(pos)
grains = 300000
for i in range(grains):
    sand = (500, 0)
    while True:
        #  if sand[1] + 1 > last:
        #    assert False, i
        if (sand[0], sand[1] + 1) not in pos:
            sand = (sand[0], sand[1] + 1)
        elif (sand[0] - 1, sand[1] + 1) not in pos:
            sand = (sand[0] - 1, sand[1] + 1)
        elif (sand[0] + 1, sand[1] + 1) not in pos:
            sand = (sand[0] + 1, sand[1] + 1)
        else:
            break
    if sand == (500, 0):
        print(i + 1)
        break
    pos.add(sand)
