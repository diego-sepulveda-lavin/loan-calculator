n = int(input())
result = []

for _ in range(n):
    number = int(input())
    if number % 7 == 0:
        result.append(number)

for element in result:
    print(element ** 2)
