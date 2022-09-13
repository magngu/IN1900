# Created by    : Magnus Gullien
# Created date  : 21. aug 2022
# Course        : UiO IN1900
# Excercise     : 2.3 population.py
# ---------------------------------------------------------------------------
# Calculates population after 24hours, given initial conditions
# ---------------------------------------------------------------------------
from math import exp, floor

#Variables given
B    = 50000    #population carrying capacity
N_t0 = 5000     #population at t0
k    = 0.2      #growth rate per hour
t1   = 24       #hours

# Find constant C
C = (B / N_t0) - 1

#Population after t1 hours
N_t1 = B / (1 + C*exp(-k*t1))
print(f'After {t1} hours, the number of bacteria is {floor(N_t1)}')


"""
Example:
>>>python3 population.py
After 24 hours, the number of bacteria is 46551
"""
