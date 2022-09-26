# Created by    : magngu@math.uio.no
# Created date  : 26. sep 2022
# Course        : UiO IN1900
# Excercise     : 6.5 oscillating_spring_A.py
# ---------------------------------------------------------------------------
# Calculate t and y = f(t), then generate plot using matplotlib
# This is part A and C of the exercise, using non-vectorized approach
# ---------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from math import cos, exp, sqrt

def y1(t, g=0.15, k=4, m=9, A=(-0.3)):
    '''
    Vertical position of object hung from a spring at time t.

    Arguments:
    t   -- Time in seconds

    Keyword arguments:
    g   -- Air friction in 1/sec
    k   -- Spring constant in kg/sec^2
    m   -- Mass of object hung from spring in kg
    A   -- Distance the object is pulled down in meters

    Returns:
    y   -- Vertical position of object in meters
    '''

    y = A*exp(-g*t) * cos(sqrt(k/m)*t)
    return y


#Declare variables
n  = 101            #Number of values to be calculated
i  = [0, 25]        #Interval of t-values
dt = (i[1] - i[0]) / (n-1)
t_array = np.zeros(n)
y_array = np.zeros(n)

#Populate arrays with data
for i in range(n):
    t_array[i] = i * dt
    y_array[i] = y1(t_array[i])

#Plot data
plt.plot(t_array, y_array, label='y(t)')
plt.legend()
plt.xlabel('t (seconds)')
plt.ylabel('y (meters)')
plt.title('Oscillating Spring, non-vectorized')
plt.show()


"""
Example:
>>>python3 oscillating_spring_A.py
~/IN1900/oscillating_spring_A.py:47: MatplotlibDeprecationWarning: The
resize_event function was deprecated in Matplotlib 3.6 and will be removed two
minor releases later. Use callbacks.process('resize_event', ResizeEvent(...))
instead.
  plt.plot(t_array, y_array, label='y(t)')

***plotted vist, matcher det vektoriserte***
"""
