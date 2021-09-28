limit_number = int(input())
current = 1

while current < limit_number:
    if current % 2 == 0:
        print(current)
    current += 1
