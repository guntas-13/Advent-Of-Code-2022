t = input()
for i in range(len(t) - 4):
    lit = []
    lit.extend([t[i], t[i + 1], t[i + 2], t[i + 3]])
    n1 = lit.count(lit[0])
    n2 = lit.count(lit[1])
    n3 = lit.count(lit[2])
    n4 = lit.count(lit[3])
    if n1 == 1 and n2 == 1 and n3 == 1 and n4 == 1:
        ans = i + 4
        break

print(ans)
