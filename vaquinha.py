total = media = cont = 0
while True:
    print('Insira os valores das doacoes:')
    x = float(input())
    cont += 1
    if x < 0:
        break
    else:
        total+=x
        media = total/cont
print(f'Total arrecadado:{total:.2f}')
print(f'Valor medio da doacao:{media:.2f}')