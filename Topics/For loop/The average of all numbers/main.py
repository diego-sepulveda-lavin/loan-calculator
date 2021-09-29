# put your python code here
a = int(input())
b = int(input())

total_sum = 0
counter = 0

for i in range(a, b + 1):
    if i % 3 == 0:
        total_sum += i
        counter += 1

mean = total_sum / counter
print(mean)
