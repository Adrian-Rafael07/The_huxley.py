maisnovo = 100
maisvelho = 0
for x in range(1,100+1):
    i = int(input())
    if i < maisnovo:
        maisnovo = i
    if i > maisvelho:
        maisvelho = i
print(f'mais novo: {maisnovo}')
print(f'mais velho: {maisvelho}')