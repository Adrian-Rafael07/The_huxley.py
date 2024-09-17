st = sm = sms = cont = f = m = ms = 0
for x in range(1,11):
    salario = float(input())
    sexo = str(input())
    st += salario
    if cont == 0 and sexo == 'm' or salario > ms and sexo == 'm':
        ms = salario
        sms = sexo
    elif cont == 0 and sexo == 'f' or salario > ms and sexo == 'f':
        ms = salario
        sms = sexo
    if sexo == 'f':
        f += 1
    elif sexo == 'm':
        m += 1
        sm += salario
    cont += 1
mediatotal = st/(m+f)
mediah = sm/m
print(m)
print(f)
print(f'{mediatotal:.1f}')
print(sms)
print(f'{mediah:.1f}')