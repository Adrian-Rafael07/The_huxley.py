def trig(t):
    r = 0
    if t < 0:
        return r
    elif 0 <= t < 150:
        r = 'DESEJAVEL'
        return r
    elif 150 <= t <= 200:
        r = 'LIMITROFE'
        return r
    elif t > 200:
        r = 'ALTO'
        return r
def col(c):
    res = 0
    if c < 0:
        return res
    elif 0 <= c < 150:
        res = 'DESEJAVEL'
        return res
    elif 150 <= c <= 170:
        res = 'LIMITROFE'
        return res
    elif c > 170:
        res = 'ALTO'
        return res
t = int(input())
c = float(input())
r = trig(t)
res = col(c)
if r == 0 or res == 0:
    print('Algum valor fora da faixa')
else:
    print(f'Triglicerideos {t} mg/dl: {r}')
    print(f'Colesterol total {c:.1f} mg/dl ({res})')