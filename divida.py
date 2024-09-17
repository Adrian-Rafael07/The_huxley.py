total = int(input())
pago = int(input())
if pago > total:
    print('(antes)', total)
    print('(depois)', 0)
else:
    while pago < total:
        print('(antes)', total)
        total -= pago
        print('(depois)',total)
    print('(antes)',pago)
    print('(depois)',0)
