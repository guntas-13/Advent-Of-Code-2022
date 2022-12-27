lit = []
while True:
    x = input()
    if x == 'quit':
        break
    lit.append(x)
crt = 0
stripe = 1
count = 0
k = 0
st = []
while k < 240:
    i = lit[count]
    st.append(stripe)
    if i == 'noop':
        if crt == stripe or crt == stripe - 1 or crt == stripe + 1:
            print("#", end='')
        else:
            print(".", end='')
        crt += 1
        count += 1
        k += 1
        if crt == 40 or crt == 80 or crt == 120 or crt == 160 or crt == 200:
            print()
            stripe += 40
    else:
        step = int(i.split()[1])
        if crt == stripe or crt == stripe - 1 or crt == stripe + 1:
            print("#", end='')
        else:
            print(".", end='')
        crt += 1
        if crt == 40 or crt == 80 or crt == 120 or crt == 160 or crt == 200:
            print()
            stripe += 40
        if crt == stripe or crt == stripe - 1 or crt == stripe + 1:
            print("#", end='')
        else:
            print(".", end='')
        stripe += step
        crt += 1
        k += 2
        count += 1
        if crt == 40 or crt == 80 or crt == 120 or crt == 160 or crt == 200:
            print()
            stripe += 40

