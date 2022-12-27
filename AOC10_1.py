lit = []
while True:
    x = input()
    if x == 'quit':
        break
    lit.append(x)
cycle_x = {}
X = 1
count = 1
for i in lit:
    if i == 'noop':
        cycle_x[str(count) + "D"] = X
        cycle_x[str(count) + "A"] = X
        count += 1
    else:
        try:
            step = int(i.split()[1])
        except:
            pass
        cycle_x[str(count) + "D"] = X
        count += 1
        cycle_x[str(count) + "D"] = X
        X += step
        cycle_x[str(count) + "A"] = X
        count += 1
value = 0
for j in range(20, 221, 40):
    print(j, cycle_x[str(j) + "D"])
    value += ((cycle_x[str(j) + "D"]) * j)
print(value)
