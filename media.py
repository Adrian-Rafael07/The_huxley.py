n =  int(input())
media = total = 0
for x in range(n):
    nota = int(input())
    total += nota
media = total / n
print(f'{media:.1f}')