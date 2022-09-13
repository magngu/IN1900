# Created by    : Magnus Gullien
# Created date  : 01. sep 2022
# Course        : UiO IN1900
# Excercise     : 4.2 sum_int.py
# ---------------------------------------------------------------------------
# Defines two functions and respective test functions
# ---------------------------------------------------------------------------

def sumint(n):
    "Returns sum of all positive integers up to n using for-loop."

    sum = 0
    for i in range(n+1):
        sum += i

    return sum


def sumint2(n):
        "Returns sum of all positive integers up to n using formula."

        return (n*(n+1)/2)

def test_sumint():
    n = 5
    exp = 15 #The correct answer
    calc = sumint(5) #The answer calculated by function
    msg = f'Expected {exp}, but got {calc}.'
    success = exp == calc
    assert success, msg

def test_sumint2():
    n = 5
    exp = 15 #The correct answer
    calc = sumint2(5) #The answer calculated by function
    msg = f'Expected {exp}, but got {calc}.'
    success = exp == calc
    assert success, msg


"""
Example:
>>> pytest sumint.py
============================= test session starts ==============================
platform darwin -- Python 3.10.1, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /Users/magnus/Dropbox/UiO/IN1900
collected 2 items

sumint.py ..                                                             [100%]

============================== 2 passed in 0.01s ===============================
"""
