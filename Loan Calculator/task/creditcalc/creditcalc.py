from math import log, pow, ceil

print('What do you want to calculate?')
print('type "n" for number of monthly payments,')
print('type "a" for annuity monthly payment amount,')
print('type "p" for loan principal:')
calculation_type = input('> ')

if calculation_type == "n":
    print('Enter the loan principal:')
    p = int(input('> '))  # Loan principal

    print('Enter the monthly payment:')
    monthly_payment = int(input('> '))  # Monthly payment

    print('Enter the loan interest:')
    i = float(input('> ')) / (12 * 100)  # Nominal monthly interest rate

    x = monthly_payment / (monthly_payment - i * p)
    num_monthly_payments = ceil(log(x, 1 + i))
    print(num_monthly_payments)

    years_number = num_monthly_payments // 12
    months_number = (num_monthly_payments - years_number * 12) // 1

    if years_number > 1:
        if months_number > 1:
            print(f'It will take {years_number} years and {months_number} months to repay this loan!')
        elif months_number == 1:
            print(f'It will take {years_number} years and {months_number} month to repay this loan!')
        else:
            print(f'It will take {years_number} years to repay this loan!')
    elif years_number == 1:
        if months_number > 1:
            print(f'It will take {years_number} year and {months_number} months to repay this loan!')
        elif months_number == 1:
            print(f'It will take {years_number} year and {months_number} month to repay this loan!')
    else:
        if months_number > 1:
            print(f'It will take {months_number} months to repay this loan!')
        elif months_number == 1:
            print(f'It will take {months_number} month to repay this loan!')

elif calculation_type == "a":
    print('Enter the loan principal:')
    p = int(input('> '))  # Loan principal

    print('Enter the number of periods:')
    n = int(input('> '))  # Number of payments

    print('Enter the loan interest:')
    i = float(input('> ')) / (12 * 100)  # Nominal monthly interest rate

    x = i * pow(1 + i, n)
    y = pow(1 + i, n) - 1
    a = ceil(p * (x / y))  # Annuity payment

    print(f'Your monthly payment = {a}!')

elif calculation_type == "p":
    print('Enter the annuity payment:')
    a = float(input('> '))  # Annuity payment

    print('Enter the number of periods:')
    n = int(input('> '))  # Number of payments

    print('Enter the loan interest:')
    i = float(input('> ')) / (12 * 100)  # Nominal monthly interest rate

    x = i * pow(1 + i, n)
    y = pow(1 + i, n) - 1
    p = round(a / (x / y))  # Loan principal

    print(f'Your loan principal = {p}!')
