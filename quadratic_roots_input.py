# Created by    : magngul@math.uio.no
# Created date  : 20. sep 2022
# Course        : UiO IN1900
# Excercise     : 5.1 quadratic_roots_input.py
# ------------------------------------------------------------------------------
# Calculates roots of polynomial provided by user input.
# ------------------------------------------------------------------------------
from math import sqrt

def quad_roots(a, b, c):
    """
    Returns real roots of quadratic polynomial as float. Does not handle
    complex solutions until later excercise.
    """
    x1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)

    return x1, x2   #floats


def welcome_msg():
    """Collection messages printed at runtime."""
    print('A quadratic polynomial has the form aX^2 + bX + C.')
    print('Enter coefficients to calculate the real roots')


#-------------------------------------------------------------------------------
welcome_msg()
try:
    a = float(input('Enter a: '))
    b = float(input('Enter b: '))
    c = float(input('Enter c: '))
except ValueError:
    print('You did not enter a number. Restart the program')
    exit()

x1, x2 = quad_roots(a, b, c)
print(f'The roots are x1 = {x1:.2} and x2 = {x2:.2}')



"""
>>>python3 quadratic_roots_input.py
A quadratic polynomial has the form aX^2 + bX + C.
Enter coefficients to calculate the real roots
Enter a: 1
Enter b: 4
Enter c: 4
The roots are x1 = -2.0 and x2 = -2.0

#Crash if complex roots due to no functionality to handle it
>>>python3 quadratic_roots_input.py
A quadratic polynomial has the form aX^2 + bX + C.
Enter coefficients to calculate the real roots
Enter a: 1
Enter b: 4
Enter c: 5
Traceback (most recent call last):
  File "/Users/magnus/Desktop/quadratic_roots_input.py", line 37, in <module>
    x1, x2 = quad_roots(a, b, c)
  File "/Users/magnus/Desktop/quadratic_roots_input.py", line 15, in quad_roots
    x1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
ValueError: math domain error
"""
