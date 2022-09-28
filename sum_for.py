# Created by    : magngul@math.uio.no
# Created date  : 31. aug 2022
# Course        : UiO IN1900
# Excercise     : 3.4 sum_for.py
# ---------------------------------------------------------------------------
# Computes sum per formula given in excercise. This is the error corrected code
# ---------------------------------------------------------------------------
"""
3 errors found:
    Error 1 - Line 17: Incorrect variable name in for loop. Changed i to k
    Error 2 - Line 17: Incorrect range(start, stop). Corrected to (1, M+1)
    Error 3 - Line 18: Missing parenthesis to raise 2*k to the 2nd power
"""
s = 0
M = 3

for k in range(1, M+1):  #Error 1 & Error 2 corrected
    s += 1/(2*k)**2      #Error 3 corrected.

print(s)


"""
Example:
>>> python3 sum_for.py
0.3402777777777778
>>>
"""
