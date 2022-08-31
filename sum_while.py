# Created by    : Magnus Gullien
# Created date  : 31. aug 2022
# Course        : UiO IN1900
# Excercise     : 3.5 sum_while.py
# ---------------------------------------------------------------------------
# Computes sum per formula given in excercise 3.4 using a while-loop.
# ---------------------------------------------------------------------------

s = 0
M = 3
k = 1

while k <= M:
    s += 1/(2*k)**2
    k += 1

print(s)


"""
Example:
>>> python3 sum_while.py
0.3402777777777778
>>>
"""
