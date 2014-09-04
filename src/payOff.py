#!/usr/bin/env python
# -*- coding: utf-8 -*-


def minPay(balance, annual_interest_rate, monthly_payment_rate, months=12):
    """
    Function calculates the credit card balance after m months
    if a person only pays the minimum monthly payment.
    """
    unpaid_balance = balance
    monthly_payment = 0.0
    month = 1
    monthly_interest_rate = annual_interest_rate / 12.0
    total_paid = 0.0

    while month <= months:
        min_payment = balance * monthly_payment_rate
        unpaid_balance = balance - min_payment
        monthly_payment = monthly_interest_rate * unpaid_balance
        balance = unpaid_balance + monthly_payment
        total_paid += min_payment

        print("Month:", month)
        print("Minimum monthly payment:", round(min_payment, 2))
        print("Remaining balance:", round(balance, 2))

        month += 1

    print("Total paid:", round(total_paid, 2))
    print("Remaining balance:", round(balance, 2))


def fixedPay(balance, annual_interest_rate):
    """
    Function calculates the minimum fixed monthly payment needed
    in order pay off a credit card balance within 1 year.
    """
    balance = float(balance)
    monthly_interest_rate = annual_interest_rate / 12.0
    month = 0
    unpaid = balance
    pre_unpaid = balance
    monthly_payment = 10.0

    while month <= 12:
        if month == 12 and unpaid > 0.0:
            monthly_payment += 10.0
            unpaid = balance
            pre_unpaid = balance
            month = 0
        elif month == 12 and unpaid <= 0.0:
            print("Lowest Payment:", int(monthly_payment))
            break
        unpaid = pre_unpaid - monthly_payment
        interest = monthly_interest_rate * unpaid
        pre_unpaid = unpaid + interest
        month += 1


def improve_fixedPay(balance, annual_interest_rate):
    """
    Improve performance by using bisection search algorithm
    """
    balance = float(balance)
    monthly_interest_rate = annual_interest_rate / 12.0

    month = 0
    unpaid = balance
    pre_unpaid = balance
    lower_bound = round(balance / 12, 2)
    upper_bound = round((balance * (1 + monthly_interest_rate)**12) / 12.0, 2)
    monthly_payment = round((lower_bound + upper_bound) / 2.0, 2)

    while month <= 12:
        if month == 12 and unpaid > 0.0:
            lower_bound = monthly_payment
            monthly_payment = round((lower_bound + upper_bound) / 2.0, 2)
            unpaid = balance
            pre_unpaid = balance
            month = 0
        # If caught in an infinite loop, attempt with a lower accuracy
        elif month == 12 and unpaid <= -0.1:
            upper_bound = monthly_payment
            monthly_payment = round((lower_bound + upper_bound) / 2.0, 2)
            unpaid = balance
            pre_unpaid = balance
            month = 0
        elif month == 12 and unpaid <= 0.0 and unpaid > -0.1:
            print("Lowest Payment:", round(monthly_payment, 2))
            break
        unpaid = pre_unpaid - monthly_payment
        interest = round(monthly_interest_rate * unpaid, 2)
        pre_unpaid = unpaid + interest
        month += 1




if __name__ == '__main__':
    balance = 999999
    annualInterestRate = 0.18
    improve_fixedPay(balance, annualInterestRate)
