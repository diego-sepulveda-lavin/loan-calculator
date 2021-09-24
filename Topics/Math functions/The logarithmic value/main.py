from math import log

a = int(input())
b = int(input())

if b > 1:
    print(round(log(a, b), 2))
else:
    print(round(log(a), 2))
