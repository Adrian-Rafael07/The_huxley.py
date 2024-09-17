def calculadora(n1,n2,n3,n4,n5):
    media = (n1+n2+n3+n4+n5)/5
    if media >= 7:
        return True
    else:
        return False
f = int(input())
n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
media = calculadora(n1,n2,n3,n4,n5)
if media==True and f <=5:
    print('APROVADO')
else:
    print('REPROVADO')