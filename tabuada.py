def n1(x):
    if x>=1:
        inicio = x
        return inicio
    elif x < 1:
            while True:
                print('Insira um número inicial entre 1 e 9')
                inicio = int(input())
                if inicio >= 1 and inicio < 9:
                    return inicio
                else:
                    continue

def n2(x):
    if x <= 9:
        final = x
        return final
    elif x > 9:
        while True:
            print('Insira um número final entre 1 e 9')
            final = int(input())
            if final <= 9 and final > inicio:
                return final
            else:
                continue
for p in range(1,3):
    x = int(input())
    if p == 1:
        inicio = n1(x)
    else:
        final = n2(x)
if final < inicio:
    print('Nenhuma tabuada nesse intervalo')
else:
    for i in range(inicio,final+1,1):
        for x in range(1,10):
            print(f'{inicio} x {x} = {inicio*x}')
        print()
        inicio += 1