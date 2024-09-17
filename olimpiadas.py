p = int(input())
pontos = int(input())
cont = 0
for i in range(0,p):
    f1 = int(input())
    f2 = int(input())
    if (f1+f2)>=pontos and f1>0 and f2>0:
        cont += 1
print(cont)