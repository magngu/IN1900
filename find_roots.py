# Created by    : Magnus Gullien
# Created date  : 22. aug 2022
# Course        : UiO IN1900
# Excercise     : 2.4 find_roots.py
# ---------------------------------------------------------------------------
# Prints roots of the hardcoded polynomial to the terminal
# ---------------------------------------------------------------------------

from math import sqrt

#Coefficients of 6x**2 - 5x + 1 = 0
a = 6
b = -5
c = 1

x1 = (-b + sqrt(b**2 -4*a*c)) / (2*a)
x2 = (-b - sqrt(b**2 -4*a*c)) / (2*a)

print(f'The roots are x1 = {x1:.2f} & x2 = {x2:.2f}')

"""
Example:
>>>python3 find_roots.py
The roots are x1 = 0.50 & x2 = 0.33
"""
