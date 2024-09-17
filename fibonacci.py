q = int(input())
b = c = 0
for x in range(q):
    print(c)
    c = c + b
    b = c - b
    if c == 0:
        c = c + 1