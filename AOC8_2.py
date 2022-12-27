def count(y, na, g):
    view = 0
    if g == 1:
        c = na[::-1]
    else:
        c = na
    for t in range(len(c)):
        view += 1
        if y <= c[t]:
            break
    return view


lit = []
while True:
    x = input()
    if x == 'quit':
        break
    lit.append(x)
size = len(lit)
lit_v = []
for i in range(size):
    lt = []
    for j in range(size):
        lt.append(lit[j][i])
    lit_v.append(''.join(lt))
final = []
ind = []
for k in range(1, size - 1):
    for l in range(1, size - 1):
        n = lit[k][l]
        top = count(n, lit_v[l][:k], 1)
        bottom = count(n, lit_v[l][(k + 1):], 0)
        left = count(n, lit[k][:l], 1)
        right = count(n, lit[k][(l + 1):], 0)
        final.append((top * bottom * left * right))
        ind.append(list((k, l)))
print(max(final))
print(ind[final.index(max(final))])
''' 
lit_v[l][:k]
lit_v[l][(k + 1):]
lit[k][:l]
lit[k][(l + 1):]
'''
