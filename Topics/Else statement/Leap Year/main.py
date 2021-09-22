# put your python code here
year = int(input())

a = 4
b = 100
c = 400

year_divisible_by_a = year % a == 0
year_divisible_by_b = year % b == 0
year_divisible_by_c = year % c == 0

if year_divisible_by_a and not year_divisible_by_b or year_divisible_by_c:
    print("Leap")
else:
    print("Ordinary")
