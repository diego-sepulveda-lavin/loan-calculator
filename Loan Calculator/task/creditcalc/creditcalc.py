loan_principal = int(input("Enter the loan principal:\n> ").strip())

type_of_calculation = input("""What do you want to calculate?
type "m" for number of monthly payments,
type "p" for the monthly payment:\n> """)

if type_of_calculation == "m":
    monthly_payment = int(input("Enter the monthly payment:\n> ").strip())
    period = -(-loan_principal // monthly_payment)
    print(f"It will take {period} {'months' if period > 1 else 'month'} to repay the loan")
elif type_of_calculation == "p":
    number_months = int(input("Enter the number of months:\n> ").strip())
    payment = -(-loan_principal // number_months)
    if payment * number_months > loan_principal:
        last_payment = loan_principal - (number_months - 1) * payment
        print(f"Your monthly payment = {payment} and the last payment = {last_payment}")
    else:
        print(f"Your monthly payment = {payment}")
