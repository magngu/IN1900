# Created by    : magngul@math.uio.no
# Created date  : 03. oct 2022
# Course        : UiO IN1900
# Excercise     : A.2 fibonacci.py
# ---------------------------------------------------------------------------
# Calculates and prints the first 15 elements of the Fibonacci sequence
# ---------------------------------------------------------------------------
import numpy as np

N = 15  # Elements to calculate
x = np.zeros(N)
x[0] = 1
x[1] = 1

# Print header & initial conditions
print(f'  n |   Xn  ')
print(f'------------')
print(f'  0 | {x[0]:5.0f}')
print(f'  1 | {x[1]:5.0f}')

#Calcualte and print rest of sequence
for n in range(2, N):  # Counting x0 as one element, if not it should be n+1
    x[n] = x[n-1] + x[n-2]
    print(f'{n:3.0f} | {x[n]:5.0f}')


"""
Example:
>>>python3 fibonacci.py
  n |   Xn
------------
  0 |     1
  1 |     1
  2 |     2
  3 |     3
  4 |     5
  5 |     8
  6 |    13
  7 |    21
  8 |    34
  9 |    55
 10 |    89
 11 |   144
 12 |   233
 13 |   377
 14 |   610
"""
