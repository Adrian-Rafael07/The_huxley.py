n = int(input())
if 1 <= n :
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,'',end='')
        print()
else:
    print()