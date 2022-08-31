# Created by    : Magnus Gullien
# Created date  : 24. aug 2022
# Course        : UiO IN1900
# Excercise     : 2.1 ball.py
# ---------------------------------------------------------------------------
# Calculates max height of a ball throw and prints it to the console
# ---------------------------------------------------------------------------

G  = 9.81   # gravitational constant
v0 = 8.2    # meter per sec
t1 = v0/G   # time of max alt

alt_t1 = v0*t1 - 0.5*G*t1**2
print(f'Max height is {alt_t1:.2f} meter')


"""
Example:
>>>python3 ball.py
Max height is 3.43 meter
"""
