a = int(input())
b = int(input())
inicio = min(a, b)
fim = max(a, b)
soma = 0
for i in range(inicio, fim + 1):
    if i > 0:
        soma += i
print(soma)
