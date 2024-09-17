a1, a2 =  input().split()
a1 = int(a1)
a2 = int(a2)
if (a2 - a1)<4:
    if a1%4==0:
        print(a1)
    elif a2%4==0:
        print(a2)
    else:
        print(-1)

else:
    for i in range(a1,a2+1):
        if (i%4==0 and i%100!=0) or i%400==0:
            print(i)
        else:
            continue