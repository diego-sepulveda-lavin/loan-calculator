args = sys.argv

# further code of the script "add_four_numbers.py"
numbers = []
for num in args[1:]:
    numbers.append(int(num))

total = sum(numbers)
print(total)
