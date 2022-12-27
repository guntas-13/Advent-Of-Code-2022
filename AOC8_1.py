lit = []
while True:
    x = input()
    if x == 'quit':
        break
    lit.append(x)
size = len(lit)
count = (size - 1) * 4
lit_v = []
for i in range(size):
    lt = []
    for j in range(size):
        lt.append(lit[j][i])
    lit_v.append(''.join(lt))
for k in range(1, size - 1):
    for l in range(1, size - 1):
        n = lit[k][l]
        cond = ((n >= max(lit[k][(l + 1):]) and (n not in lit[k][(l + 1):])) or (
                n >= max(lit_v[l][(k + 1):]) and (n not in lit_v[l][(k + 1):])) or (
                        n >= max(lit[k][:l]) and (n not in lit[k][:l])) or (
                        n >= max(lit_v[l][:k]) and (n not in lit_v[l][:k])))
        if cond:
            count += 1
print(count)
