n=c=q=0
while True:
    v=int(input())
    if v==0:
        break
    if v==5:
        c+=1
    elif v==9:
        n+=1
    elif v==4:
        q+=1
if n>c and c>q:
    print('canal 9:',n)
    print('canal 5:', c)
    print('canal 4:', q)
elif n>q and q>c:
    print('canal 9:',n)
    print('canal 4:', q)
    print('canal 5:', c)
elif c>n and n>q:
    print('canal 5:',c)
    print('canal 9:',n)
    print('canal 4:',q)
elif c>q and q>n:
    print('canal 5:',c)
    print('canal 4:',q)
    print('canal 9:',n)
elif q>n and n>c:
    print('canal 4:', q)
    print('canal 9:', n)
    print('canal 5:', c)
elif q>c and c>n:
    print('canal 4:', q)
    print('canal 5:', c)
    print('canal 9:', n)