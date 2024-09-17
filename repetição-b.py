cont = media = total = 0
while True:
    x=int(input())
    if x == 0:
        break
    cont+=1
    total += x
    media = total/cont
print(f'{media:.0f}')