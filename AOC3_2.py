lit = []
while True:
    x = input()
    lit.append(x)
    if x == 'quit':
        break
st = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
sm = 0
for i in range(0, len(lit) - 3, 3):
    pf = set(lit[i]) & set(lit[i + 1]) & set(lit[i + 2])
    print(pf)
    sm += st.index(list(pf)[0]) + 1

print(sm)
