string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'

total_vowels = 0

for char in string:
    if char in vowels:
        total_vowels += 1

print(total_vowels)
