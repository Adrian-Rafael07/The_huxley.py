ano = vel = cont = maiorano = maiorvel = soma = 0
while True:
    m = input().lower().strip()
    if m == 'n' and cont > 0:
        break
    elif m == 'n' and cont == 0:
        print('zero')
        break
    ano = int(input())
    vel = float(input())
    cont += 1
    soma += vel
    media = soma / cont
    if cont == 1:
        maiorano = ano
    else:
        if maiorano < ano:
            maiorano = ano
    if cont == 1:
        maiorvel = vel
    else:
        if maiorvel < vel:
            maiorvel = vel
if cont>=1:
    print(f'{maiorvel:.2f}')
    print(maiorano)
    print(f'{media:.2f}')
