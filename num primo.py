while True:
    num = int(input())
    if num == -1:
        break
    if num <= 1:
        print(0)
    elif num <= 3:
        print(1)
    elif num % 2 == 0 or num % 3 == 0:
        print(0)
    else:
        i = 5
        is_prime = True
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                is_prime = False
                break
            i += 6
        print(1 if is_prime else 0)
        