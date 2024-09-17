aprovado = 0
while True:
    portugues = int(input())
    if portugues < 0:
        break
    else:
        matematica = int(input())
        redacao = float(input())
        if portugues >= 40 and matematica >= 21 and redacao >=7:
            aprovado += 1
print(aprovado)