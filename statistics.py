# Created by    : magngul@math.uio.no 
# Created date  : 12. sep 2022
# Course        : UiO IN1900
# Excercise     : 4.8 statistics.py
# -----------------------------------------------------------------------------
# Functions to calculate mean and std.deviation with respective test functions.
# -----------------------------------------------------------------------------
from math import sqrt
import numpy as np

def mean(x_list):
    """Takes a list with numbers and returns the mean value as float."""
    sum = 0
    for x in x_list:
        sum += x

    return sum/len(x_list)  # Mean


def standard_deviation(x_list):
    """Takes a list of numbers and returns the standard deviation as float."""
    sum = 0
    x_mean = mean(x_list)
    for x in x_list:
        sum += (x - x_mean)**2

    return sqrt(sum/len(x_list))    #Standard deviation


def test_standard_deviation():
    """Test function for standard_deviation()"""
    x_test  = [0.699, 0.703, 0.698, 0.701]
    expect  = np.std(x_test)
    calc    = standard_deviation(x_test)
    tol     = 1e-14 #tolerance for float comparison
    success = (expect - calc) < tol
    msg = f'Expected {expect} but got {calc}.'

    assert success, msg


def test_mean():
    """Test function for mean()"""
    x_test  = [0.699, 0.703, 0.698, 0.701]
    expect  = np.mean(x_test)
    calc    = mean(x_test)
    tol     = 1e-14 #tolerance for float comparison
    success = (expect - calc) < tol
    msg = f'Expected {expect} but got {calc}.'

    assert success, msg


"""
Example:
>>>pytest statistics.py
============================= test session starts ==============================
platform darwin -- Python 3.10.1, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: ~/IN1900
collected 2 items

statistics.py ..                                                         [100%]

============================== 2 passed in 0.10s ===============================
"""
