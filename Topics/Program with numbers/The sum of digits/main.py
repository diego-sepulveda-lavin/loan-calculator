# put your python code here
number = int(input())

hundreds = number // 100
tens = number // 10 % 10
units = number % 10

digits_sum = hundreds + tens + units

print(digits_sum)
