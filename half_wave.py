# Created by    : Magnus Gullien
# Created date  : 11. sep 2022
# Course        : UiO IN1900
# Excercise     : 4.5 half_wave.py
# ---------------------------------------------------------------------------
# Implements half-wave rectifier funtion and associated test function
# ---------------------------------------------------------------------------

from math import pi, sin

def f(x):
    """Half-wave rectifier for sin(x). sin(x)<=0 is set to 0. Returns float."""

    if sin(x) > 0:
        return sin(x)
    else:
        return 0


def test_f():
    """Test function for f(x)."""
    x1, x2       = 0, pi/2
    exp1, exp2   = 0, 1         #Expected values
    calc1, calc2 = f(x1), f(x2) #Values returned by f(x)

    msg = f'Expected {exp1} & {exp2}, but got {calc1} & {calc2}.'
    success = exp1 == calc1 and exp2 == calc2
    assert success, msg


"""
Example:
>>>pytest half_wave.py
============================= test session starts ==============================
platform darwin -- Python 3.10.1, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: ~/IN1900
collected 1 item

half_wave.py .                                                           [100%]

============================== 1 passed in 0.01s ===============================
"""
