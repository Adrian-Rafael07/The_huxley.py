pi = int(input())
ai = int(input())
q = int(input())
af = int(input())

mult = (q/100)+1
result = pi

while ai <= af:
    print(ai, end=' ')
    print(int(result))
    result *= mult
    ai += 1
