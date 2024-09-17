e = int(input())
n1 = 1
n2 = 3
if e == 0:
    print(0.00)
else:
    print(f'{n1}/{n2}',end='')
    for i in range(1,e):
        n1 += 1
        n2 += 3
        print(f' + {n1}/{n2}',end='')
    print(f'\n{0.333333*e:.2f}')