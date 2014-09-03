# Problem set 2

<br>

## Overview - Paying off credit card debt

Assume that you have made a $5,000 purchase on a credit card
with an 18% annual interest and a 2% minimum monthly payment rate.
If you only pay the minimum monthly amount for a year,
how much is the remaining balance?

You can think about this in the following way.

At the beginning of month 0 (when the credit card statement arrives),
assume you owe an amount we will call `b0`
(`b` for balance; `0` to indicate this is the balance at month 0).

Any payment you make during that month is deducted from the balance.
Let's call the payment you make in month 0, `p0`.
Thus, your __unpaid balance__ for month 0, `ub0`. `ub0 = b0 - p0`.

At the beginning of month 1, the credit card company will charge you interest
on your unpaid balance. So if your annual interest rate is `r`,
then at the beginning of month 1, your new balance would be
`b1 = ub0 + r/12.0 * ub0`.

In month 1, we will make another payment, `p1`.
That payment has to cover some of the interest costs,
so it does not completely go towards paying off the original charge.
The balance at the beginning of month 2, `b2`,
can be calculated by first calculating the unpaid balance after paying `p1`,
then by adding the interest accrued: `ub1 = b1 - p1; b2 = ub1 + r/12.0 * ub1`.

If you choose just to pay off the minimum monthly payment each month,
you will see that the compound interest will dramatically reduce your ability
to lower your debt.

Let's look at an example. If your have got a $5,000 balance on a credit card
with 18% annual interest rate, and the minimum monthly payment is 2%
of the current balance, we would have the following repayment schedule if you
only pay the minimum payment each month.

<table class="table table-bordered table-striped table-condensed">
<tr>
<td>Month</td>
<td>Balance</td>
<td>Minimum Payment</td>
<td>Unpaid Balance</td>
<td>Interest</td>
</tr>

<tr>
<td>0</td>
<td>5000.00</td>
<td>100<br><code>5000 x 0.02</code></br></td>
<td>4900<br><code>5000 - 100</code></br></td>
<td>73.50<br><code>0.18/12.0 x 4900</code></br></td>
</tr>

<tr>
<td>1</td>
<td>4973.50<br><code>4900 + 73.50</code></br></td>
<td>99.47<br><code>4973.50 x 0.02</code></br></td>
<td>4874.03<br><code>4973.50 - 99.74</code></br></td>
<td>73.11<br><code>0.18/12.0 x 4874.03</code></br></td>
</tr>

<tr>
<td>2</td>
<td>4947.14<br><code>4874.03 + 73.11</code></br></td>
<td>98.94<br><code>4947.14 x 0.02</code></br></td>
<td>4848.20<br><code>4947.14 - 98.94</code></br></td>
<td>72.72<br><code>0.18/12.0 x 4848.20</code></br></td>
</tr>
</table>

You can see that a lot of your payment is going to cover interest,
and if you work this through month 12,
you will see that after a year, you will have paid $1,165.63
and yet you will still owe $4,691.11 on what was originally
a $5,000.00 debt. Pretty depressing!

<br>

## Problem 1: Paying the minimum

Write a program to calculate the credit card balance after one year
if a person only pays the minimum monthly payment
required by the credit card company each month.

The following variables contain values as described below:

1. `balance` - the outstanding balance on the credit card
2. `annualInterestRate` - annual interest rate as a decimal
3. `monthlyPaymentRate` - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment
and remaining balance, and print to screen something of the format
(_Be sure to print out no more than two decimal digits of accuracy_):

```
Month: 1
Minimum monthly payment: 96.00
Remaining balance: 4784.00
```

Finally, print out the total amount paid that year
and the remaining balance at the end of the year in the format:

```
Total paid: 1165.63
Remaining balance: 4691.11
```

<br>

#### A summary of the required math is found below:

- Monthly interest rate - `monthlyInterestRate = annualInterestRate / 12.0`
- Minimum monthly payment - `minimumMonthlyPayment = monthlyPaymentRate * previousBalance`
- Monthly unpaid balance - `monthlyUnpaidBalance = previousBalance - minimumMonthlyPayment`
- Updated balance each month - `monthlyUnpaidBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalnce`

<br>

#### How to think about this problem?

- For each month:
 1. Compute the monthly payment, based on the previous month's balance.
 2. Update the outstanding balance by removing the payment, then charging interest on the result.
 3. Output the monthly summary.
 4. Keep track of the total amount of paid over all the past months so far.
- Print out the total result.
