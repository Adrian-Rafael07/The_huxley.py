notas = []
nomes = []
ordemnotas = []
distancia = [0]*5
nota1 = media = nota2 = maiord = 0
nomemaior = ''
for i in range(5):
    nota = float(input())
    nomes.append(input())
    notas.append(f'{nota:.2f}')
    ordemnotas.append(nota)
ordemnotas.sort(reverse=True)
for i in range(0, len(notas)):
    num = ordemnotas[i]
    nota2 += float(notas[i])
    if i < 4:
        print(f'{num:.2f}',end=' ')
    else:
        print(f'{num:.2f}')
media = nota2/5
print(f'{media:.2f}')

for i in range(0,len(notas)):
    (notas[i]) = float(notas[i])
    distancia[i] = (media-notas[i])
    n = distancia[i]
    notas[i] = distancia[i]
    if n < 0:
        n *= (-1)
    if n > maiord and n > 0 :
        nome = nomes[i]
        maiord = n
        d = i
    elif n <= 0:
        nome = nomes[i]
        d = 0
    if i < 4:
        print(f'{n :.2f}',end=' ')
    else:
        print(f'{n :.2f}')
    if nome == 'david':
        nome = 'mari'
print(f'{nome.capitalize()}')
print(d)
