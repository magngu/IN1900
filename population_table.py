# Created by    : magngul@math.uio.no
# Created date  : 31. aug 2022
# Course        : UiO IN1900
# Excercise     : 3.7 population_table.py
# ---------------------------------------------------------------------------
# Computes population P(t) and prints table with t and P(t)
# ---------------------------------------------------------------------------
from math import exp

n  = 12
dt = 48/(n+1)   #Interval length, hours
P  = lambda t: 50000 / (1 + 9*exp(-0.2*t)) #Growth formula, taken from ex 2.3

#Calculates t and N and stores result in two lists
t = []
N = []
for i in range(n+1):
    t.append(i*dt)
    N.append(P(t[i]))

# Print results as a nicely formated table
print('|--------------------------|')
print('|  POPULATION GROWTH TABLE |')
print('|--------------------------|')
print('|   t hours  |     N(t)    |')
print('|--------------------------|')
for el in range(len(t)):
    print(f'| {t[el]:8.2f}   |  {N[el]:8.2f}   |')
print('|--------------------------|')


"""
Example:
>>>python3 population_table.py
|--------------------------|
|  POPULATION GROWTH TABLE |
|--------------------------|
|   t hours  |     N(t)    |
|--------------------------|
|     0.00   |   5000.00   |
|     3.69   |   9432.83   |
|     7.38   |  16366.33   |
|    11.08   |  25226.99   |
|    14.77   |  34030.99   |
|    18.46   |  40842.00   |
|    22.15   |  45161.08   |
|    25.85   |  47564.67   |
|    29.54   |  48805.91   |
|    33.23   |  49422.20   |
|    36.92   |  49722.22   |
|    40.62   |  49866.88   |
|    44.31   |  49936.30   |
|--------------------------|
>>>
"""
