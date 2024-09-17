def verif(x):
    if x % 3 == 0:
        return True
    else:
        return False


def fatorial(fator):
    soma = 1
    for i in range(1, fator + 1):
        soma = soma * i
        return soma


def resultado():
    print()

for i in range(0,5):
    x = int(input())
    retorno = verif(x)
    if retorno == True:
        fator = x
        fator1 = fatorial(fator)