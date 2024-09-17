def decisor(k,v):
    kp = 0
    vp = 0
    if k == 'PEDRA' and v == 'TESOURA' or k == 'TESOURA' and v == 'PAPEL' or k == 'PAPEL' and v == 'PEDRA':
        kp += 1
        return True
    elif v == 'PEDRA' and k == 'TESOURA' or v == 'TESOURA' and k == 'PAPEL' or v == 'PAPEL' and k == 'PEDRA':
        vp += 1
        return False

q = int(input())
kp = vp = 0
for x in range(0,q):
    k = str(input()).upper()
    v = str(input()).upper()
    r = decisor(k,v)
    if r:
        kp += 1
    elif r == False:
        vp += 1
if kp > vp:
    print('VINICIUS VAI LAVAR A LOUÇA!')
elif kp < vp:
    print('KYARA VAI LAVAR A LOUÇA!')
elif kp == vp:
    print('OS DOIS VÃO LAVAR A LOUÇA JUNTOS!')