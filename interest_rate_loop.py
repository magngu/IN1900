# Created by    : Magnus Gullien
# Created date  : 01. sep 2022
# Course        : UiO IN1900
# Excercise     : 3.12 interest_rate_loop.py
# ---------------------------------------------------------------------------
# Calculates number of years required to reach desired amount from interest
# ---------------------------------------------------------------------------
initial_amount = 100
r = 5.5 # interest rate
amount = initial_amount
years = 0

while amount <= 1.5*initial_amount:
    amount +=  r/100*amount
    years +=  1

print(years)

"""
Example:
>>>python3 interest_rate_loop.py
8

What problem does this program solve?
This program solved a exponential equation of the forn a^n = b for n.
"""
