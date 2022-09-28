# Created by    : magngul@math.uio.no
# Created date  : 21. aug 2022
# Course        : UiO IN1900
# Excercise     : 2.2 interest_rate.py
# ---------------------------------------------------------------------------
# Computes growth of a 1000¢ deposit over 3 years with 5% interest rate
# ---------------------------------------------------------------------------

P = 1000    #Initial deposit, Euros
r = 5.0     #interest rate in %
n = 3       #years
A = P*(1 + r/100)**n

print(f'In {n} years your {P}¢ deposit has grown to {A:.2f}¢!')


"""
Example:
>>> python3 interest_rate.py
In 3 years your 1000¢ deposit has grown to 1157.63¢!
"""
