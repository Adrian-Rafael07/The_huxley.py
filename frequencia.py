x, y = input().split()
x = int(x)
y = int(y)
q = 0
for i in range(1,x+1):
    s = int(input())
    if s == y:
        q += 1

print(q)