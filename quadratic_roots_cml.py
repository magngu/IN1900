# Created by    : magngul@math.uio.no 
# Created date  : 20. sep 2022
# Course        : UiO IN1900
# Excercise     : 5.2 quadratic_roots_cml.py
# ------------------------------------------------------------------------------
# Calculates roots of quadratic polynomial provided through the cmd line
# ------------------------------------------------------------------------------
from math import sqrt
import sys

def quad_roots(a, b, c):
    """
    Returns real roots of quadratic polynomial as float. Does not handle
    complex solutions until later excercise.
    """
    x1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)

    return x1, x2   #floats


#-------------------------------------------------------------------------------
try:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])

except IndexError:  #If less than 3 args are given in cmd line
    print('You did not provide 3 coefficients. Restart program.')
    exit()

except ValueError:  #If anything but a number is entered
    print('You did not enter a number. Restart program')
    exit()

x1, x2 = quad_roots(a, b, c)
print(f'The roots are x1 = {x1:.2} and x2 = {x2:.2}')



"""
>>>python3 quadratic_roots_cml.py 1 4 4
The roots are x1 = -2.0 and x2 = -2.0

>>>python3 quadratic_roots_cml.py 1
You did not provide 3 coefficients. Restart program

#Crash since there is no functionality to handle complex roots
>>>python3 quadratic_roots_cml.py 1 4 5
Traceback (most recent call last):
  File "/Users/magnus/Desktop/quadratic_roots_cml.py", line 36, in <module>
    x1, x2 = quad_roots(a, b, c)
  File "/Users/magnus/Desktop/quadratic_roots_cml.py", line 16, in quad_roots
    x1 = (-b + sqrt(b**2 - 4*a
"""
