# Created by    : Magnus Gullien
# Created date  : 11. sep 2022
# Course        : UiO IN1900
# Excercise     : 4.1 pop_func.py
# ---------------------------------------------------------------------------
# Implements function for population growth and prints results in table
# ---------------------------------------------------------------------------
from math import exp

def population(t, k, B, C):
    "Returns population (float) for time t."

    return B / (1+C*exp(-k*t))


def header():
    "Prints header for population table"
    print('|--------------------------|')
    print('|  POPULATION GROWTH TABLE |')
    print('|--------------------------|')
    print('|   t hours  |     N(t)    |')
    print('|--------------------------|')


def footer():
    "Prints footer for population table"
    print('|--------------------------|')
    print('| N rounded to nearest int |')
    print('|--------------------------|')


#Variables
B  = 50000   #Population carriage capacity from ex 3.7
C  = 9       #Constant taken from ex 3.7
k  = 0.2     #growth rate from ex 3.7
n  = 12
t  = [0, 48] #Hours, closed interval
dt = (t[1]-t[0])/n


#Prints table with population at times t
header()
for t in range(n+1):
    t1 = t*dt
    N = population(t1, k, B, C)
    print (f'|   {t1:6.1f}   | {N:8.0f}    | ')
footer()


"""
Example:
>>>python3 pop_func.py
|--------------------------|
|  POPULATION GROWTH TABLE |
|--------------------------|
|   t hours  |     N(t)    |
|--------------------------|
|      0.0   |     5000    |
|      4.0   |     9913    |
|      8.0   |    17749    |
|     12.0   |    27526    |
|     16.0   |    36580    |
|     20.0   |    42924    |
|     24.0   |    46552    |
|     28.0   |    48390    |
|     32.0   |    49263    |
|     36.0   |    49666    |
|     40.0   |    49849    |
|     44.0   |    49932    |
|     48.0   |    49970    |
|--------------------------|
| N rounded to nearest int |
|--------------------------|
"""
