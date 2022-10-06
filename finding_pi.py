# Created by    : magngul@math.uio.no
# Created date  : 05. oct 2022
# Course        : UiO IN1900
# Excercise     : A.4 finding_pi.py
# ---------------------------------------------------------------------------
# Approximates pi using Netwons method
# ---------------------------------------------------------------------------
import numpy as np

# Declare variables
n  = 2
f  = lambda x: np.sin(x)
df = lambda x: np.cos(x)        #Derivative of f
x  = np.zeros(n+1)
x[0] = 3.14                     #Initial condition
y  = np.pi                      #Numpy representation of pi


# Estimate pi using newtons method
for n in range(1, n+1):
    x[n] = x[n-1] - f(x[n-1])/df(x[n-1])


#Print table with approximations
#Header
print(f'------------------------------------------------')
print(f'|  Xn  |       Value       |  Diff. to np.pi   |')
print(f'------------------------------------------------')
#Content
for n in range(len(x)):
    print(f'|  X{n}  |  {x[n]:14.13f}  |  {abs(x[n]-y):15.13f}  |')
#Footer
print(f'------------------------------------------------')
print(f'| Np.pi|  {y:.13f}  |         -         |')
print(f'------------------------------------------------')


"""
Example:
>>>python3 finding_pi.py
------------------------------------------------
|  Xn  |       Value       |  Diff. to np.pi   |
------------------------------------------------
|  X0  |  3.1400000000000  |  0.0015926535898  |
|  X1  |  3.1415926549364  |  0.0000000013466  |
|  X2  |  3.1415926535898  |  0.0000000000000  |
------------------------------------------------
| Np.pi|  3.1415926535898  |         -         |
------------------------------------------------
"""
