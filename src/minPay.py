#!/usr/bin/env python
# -*- coding: utf-8 -*-


def calc(balance, annual_interest_rate, monthly_payment_rate, months=12):
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




if __name__ == '__main__':
    balance = 4842
    annualInterestRate = 0.2
    monthlyPaymentRate = 0.04

    calc(balance, annualInterestRate, monthlyPaymentRate)
