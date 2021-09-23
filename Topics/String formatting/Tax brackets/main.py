income = int(input().strip())

highest_income = 132_407
high_income = 42_708
medium_income = 15_528
low_income = 0

highest_income_tax = 0.28
high_income_tax = 0.25
medium_income_tax = 0.15
low_income_tax = 0

if income >= highest_income:
    tax_to_pay = round(income * highest_income_tax)
    tax = int(highest_income_tax * 100)
elif income >= high_income:
    tax_to_pay = round(income * high_income_tax)
    tax = int(high_income_tax * 100)
elif income >= medium_income:
    tax_to_pay = round(income * medium_income_tax)
    tax = int(medium_income_tax * 100)
else:
    tax_to_pay = round(income * low_income_tax)
    tax = int(low_income_tax * 100)
print(f"The tax for {income} is {tax}%. That is {tax_to_pay} dollars!")
