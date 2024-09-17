e = int(input())
total = total1 = 0
x = 2
y = 4
for n in range(1,e+1):
    total = e/(x*y)
    total1 += total
    x += 4
    y += 4
    e -= 1
print(f'{total1:.4f}')