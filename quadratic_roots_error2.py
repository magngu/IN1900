# Created by    : magngul@math.uio.no
# Created date  : 20. sep 2022
# Course        : UiO IN1900
# Excercise     : 5.4 quadratic_roots_error2.py
# ------------------------------------------------------------------------------
# Calculates roots of quadratic polynomial provided through user input
# ------------------------------------------------------------------------------
from math import sqrt

def quad_roots(a, b, c):
    """
    Returns real roots of a quadratic polynomial as float.
    Catches exception if solutions is complex, but does not solve for it.
    """
    if (b**2 - 4*a*c) < 0:    #Catches if roots are complex
        raise ValueError('Woops, this polynomial has no real roots.')
    else:
        x1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
        x2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)

    return x1, x2


def welcome_msg():
    """Collection of startup messages."""
    print('A quadratic polynomial has the form aX^2 + bX + C.')
    print('Enter coefficients to calculate the real roots')


#-------------------------------------------------------------------------------
#Get coefficients from user input
welcome_msg()
try:
    a = float(input('Enter a: '))
    b = float(input('Enter b: '))
    c = float(input('Enter c: '))
except ValueError:
    print('You did not enter a number. Restart the program')
    exit()

#Calculate roots of quadratic polynomial
try:
    x1, x2 = quad_roots(a, b, c)
    print(f'The roots are x1 = {x1:.2} and x2 = {x2:.2}')
except ValueError as e: #If complex roots
    print(e)
    exit()


"""
Example:
>>>python3 quadratic_roots_error2.py
A quadratic polynomial has the form aX^2 + bX + C.
Enter coefficients to calculate the real roots
Enter a: 1
Enter b: 4
Enter c: 4
The roots are x1 = -2.0 and x2 = -2.0

>>>python3 quadratic_roots_error2.py
A quadratic polynomial has the form aX^2 + bX + C.
Enter coefficients to calculate the real roots
Enter a: 1
Enter b: 1
Enter c: 1
Woops, this polynomial has no real roots.
"""
