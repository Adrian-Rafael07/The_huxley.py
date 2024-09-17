def quadrado(a):
    soma = a * a
    return soma
def retangulo(b,h):
    soma = b * h
    return soma
def circulo(raio):
    soma = (raio*raio) * 3.14
    return soma
def quantc(qc,cont):
    media = (qc/cont)*100
    return media
cont = 0
maiorq = maiorr = maiorc = qc = 0
while True:
    t = str(input()).lower()
    if t == 'sair':
        media = quantc(qc, cont)
        break
    cont += 1
    if t == 'q':
        a = int(input())
        if a < 0:
            maiorq = a
        else:
            rq = quadrado(a)
            if cont==1 or rq > maiorq:
                maiorq = rq
            elif rq > maiorq:
                maiorq = rq

    elif t == 'r':
        b = int(input())
        h = int(input())
        if b < 0 or h < 0:
            maiorr = -1
        else:
            rr = retangulo(b,h)
            if cont==1 or rr > maiorr:
                maiorr = rr
            elif rr > maiorr:
                maiorr = rr

    elif t == 'c':
        raio = int(input())
        qc += 1

        if raio < 0:
            maiorc = -1
        else:
            rc = circulo(raio)
            if cont==1 or rc > maiorc:
                maiorc = rc
            elif rc > maiorc:
                maiorc = rc


print(f'Maior circulo: {maiorc:.2f}')
print(f'Maior retangulo: {maiorr:.2f}')
print(f'Maior quadrado: {maiorq:.2f}')
print(f'Quantidade de figuras {cont}')
print(f'Percentual de circuitos: {media:.2f}')