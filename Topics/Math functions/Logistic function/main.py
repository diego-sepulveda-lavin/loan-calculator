from math import e, pow

a = int(input())

result = 1 / (1 + pow(e, -a))

print(round(result, 2))
