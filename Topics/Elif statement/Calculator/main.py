# put your python code here
a = float(input())
b = float(input())
operator = input()

# +, -, /, *, mod, pow, div
result = None
if operator == '+':
    result = a + b
elif operator == '-':
    result = a - b
elif operator == '/':
    result = "Division by 0!" if b == 0 else a / b
elif operator == '*':
    result = a * b
elif operator == 'mod':
    result = "Division by 0!" if b == 0 else a % b
elif operator == 'pow':
    result = a ** b
elif operator == 'div':
    result = "Division by 0!" if b == 0 else a // b

print(result)
