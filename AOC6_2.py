t = input()
for i in range(len(t) - 14):
    lit = []
    for j in range(14):
        lit.append(t[i + j])
    ct = []
    for n in lit:
        ct.append(lit.count(n))
    if sum(ct) == 14:
        ans = i + 14
        break

print(ans)
