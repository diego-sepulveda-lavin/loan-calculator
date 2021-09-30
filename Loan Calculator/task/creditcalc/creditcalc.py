from math import log, pow, ceil
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--type", choices=["annuity", "diff"])
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()
type_arg = args.type
payment_arg = args.payment
principal_arg = args.principal
periods_arg = args.periods
interest_arg = args.interest


def format_input_data(principal, payment, periods, interest):
    principal = principal and int(principal)
    payment = payment and float(payment)
    periods = periods and int(periods)
    interest = interest and float(interest) / (12 * 100)
    return [principal, payment, periods, interest]


def diff_payments_calc(principal, periods, interest):
    total_payment = 0

    for month in range(1, periods + 1):
        x = principal - ((principal * (month - 1)) / periods)
        monthly_diff_payment = ceil((principal / periods) + interest * x)
        total_payment += monthly_diff_payment
        print(f"Month {month}: payment is {monthly_diff_payment}")
    print()
    print(f"Overpayment = {total_payment - principal}")


def loan_principal_calc(payment, periods, interest):
    x = interest * pow(1 + interest, periods)
    y = pow(1 + interest, periods) - 1
    principal = round(payment / (x / y))

    print(f'Your loan principal = {principal}!')
    print(f"Overpayment = {round((payment * periods) - principal)}")


def annuity_payment_calc(principal, periods, interest):
    x = interest * pow(1 + interest, periods)
    y = pow(1 + interest, periods) - 1
    annuity_payment = ceil(principal * (x / y))

    print(f'Your annuity payment = {annuity_payment}!')
    print(f'Overpayment = {periods * annuity_payment - principal}!')


def total_monthly_payments_calc(principal, payment, interest):
    x = payment / (payment - interest * principal)
    num_monthly_payments = ceil(log(x, 1 + interest))
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
    total_payment = round(num_monthly_payments * payment)
    print(f"Overpayment = {total_payment - principal}")


def check_negative_inputs(payment, principal, periods):
    is_payment_negative = payment and payment < 0
    is_principal_negative = principal and principal < 0
    is_periods_negative = periods and periods < 0

    if is_payment_negative or is_principal_negative or is_periods_negative:
        return True
    return False


def calculator(calc_type, principal, payment, periods, interest):
    principal, payment, periods, interest = format_input_data(principal, payment, periods, interest)

    if (not calc_type) or (calc_type == 'diff' and payment) or (not interest):
        print("Incorrect parameters")
        return

    invalid_inputs = check_negative_inputs(payment, principal, periods)
    if invalid_inputs:
        print("Incorrect parameters")
        return

    if calc_type == "annuity":
        if payment and principal:
            total_monthly_payments_calc(principal, payment, interest)
        elif payment and periods:
            loan_principal_calc(payment, periods, interest)
        elif principal:
            annuity_payment_calc(principal, periods, interest)
    elif calc_type == "diff":
        diff_payments_calc(principal, periods, interest)


calculator(type_arg, principal_arg, payment_arg, periods_arg, interest_arg)
