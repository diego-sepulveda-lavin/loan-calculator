deposit = int(input())
max_return_amount = 700_000
interest_rate = 0.071
years = 0

while deposit < max_return_amount:
    deposit = deposit * (1 + interest_rate)
    years += 1

print(years)
