# Created by    : magngul@math.uio.no 
# Created date  : 20. sep 2022
# Course        : UiO IN1900
# Excercise     : 5.3 quadratic_roots_error.py
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
coeff = [] #Coefficients of polynomial

# Collects arguments from cmd line
try:
    coeff.append(float(sys.argv[1]) ) #aX^2
    coeff.append(float(sys.argv[2]) ) #bX
    coeff.append(float(sys.argv[3]) ) #C

except ValueError:  #If anything but a number is entered on the cmd line
    print('You did not enter a number. Restart program')
    exit()

except IndexError: # If less than 3 arguments are provided in cmd line
    missing = 4 - len(sys.argv) #Num of args not entered
    print(f'You did only provide {3-missing} coefficients, but 3 are needed.')

    #Requests coefficients from user until a total of 3 is provided
    while len(coeff) <=2:
        try:
            temp = float(input(f'Please enter the next coefficient: '))
            coeff.append(temp)

        except ValueError: #If anything but number is given as input
            print('You must enter a number, try again.')
            continue

#Calculate roots and print them
x1, x2 = quad_roots(coeff[0], coeff[1], coeff[2])
print(f'The roots are x1 = {x1:.2} and x2 = {x2:.2}')


"""
Example:
>>>python3 quadratic_roots_error.py 1 4 4
The roots are x1 = -2.0 and x2 = -2.0

>>>python3 quadratic_roots_error.py 1
You did only provide 1 coefficients, but 3 are needed.
Please enter the next coefficient: 4
Please enter the next  coefficient: -6
The roots are x1 = 1.2 and x2 = -5.2

>>>python3 quadratic_roots_error.py 1
You did only provide 1 coefficients, but 3 are needed.
Please enter the next coefficient: a
You must enter a number, try again.
Please enter the next coefficient: b
You must enter a number, try again.
Please enter the next coefficient: 4
Please enter the next coefficient: c
You must enter a number, try again.
Please enter the next coefficient: 4
The roots are x1 = -2.0 and x2 = -2.0
"""
