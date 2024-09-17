q = int(input())
if q == 0:
    print('Informe um numero positivo')
else:
    qf = qm = total = c = 0
    for x in range(1,q+1):
        s = str(input()).upper()
        v = int(input())
        if s == 'M':
            qm += 1
        elif s == 'F':
            qf += 1
        if v <= 24 :
            c+=1
        total += 1
    mediac = (c/total)*100
    mediaf = (qf/total)*100
    mediam = (qm/total)*100
    print(f'{mediaf:.1f}%')
    print(f'{mediam:.1f}%')
    print(f'{mediac:.1f}%')