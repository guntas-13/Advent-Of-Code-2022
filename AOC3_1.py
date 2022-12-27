lit = []
while True:
    x = input()
    lit.append(x)
    if x == 'quit':
        break
st = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
sm = 0
for i in lit[:-1]:
    p1 = set(i[:int(len(i) / 2)])
    p2 = set(i[int(len(i) / 2):])
    pf = p1 & p2
    sm += st.index(list(pf)[0]) + 1

print(sm)
