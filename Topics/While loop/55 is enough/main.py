# put your code here
input_counter = 0
total_sum = 0
searched_number = 55

while True:
    entered_number = int(input())
    if entered_number == searched_number:
        break
    input_counter += 1
    total_sum += entered_number

average = round(total_sum / input_counter)

print(input_counter)
print(total_sum)
print(average)
