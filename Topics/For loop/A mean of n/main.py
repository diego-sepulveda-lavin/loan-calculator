n = int(input())
total_sum = 0
counter = 0

for _ in range(n):
    number = int(input())
    total_sum += number
    counter += 1

mean = total_sum / counter
print(mean)
