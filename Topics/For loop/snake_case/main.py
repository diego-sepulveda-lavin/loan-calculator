text = input()
index = 0
under_string = "_"
output = ""

for char in text:
    if char.isupper() and index != 0:
        output += under_string
    output += char.lower()
    index += 1

print(output)
