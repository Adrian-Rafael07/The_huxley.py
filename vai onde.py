d = v = menorvalor = cont = maiord = passagem = 0
while True:
    nome = str(input()).upper()
    if cont == 0 and nome=='FIM':
        print('SEM DESTINO')
        break
    elif nome == 'FIM':
        print(cidade)
        break
    else:
        d = int(input())
        v = int(input())
        passagem = v + v
        if passagem>=300:
            print('SEM DESTINO')
            break
        if cont == 0 or d > maiord and v < menorvalor:
            menorvalor = v
            maiord = d
            cidade = nome

    cont+=1
