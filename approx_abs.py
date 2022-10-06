# Created by    : magngul@math.uio.no
# Created date  : 26. sep 2022
# Course        : UiO IN1900
# Excercise     : 6.13 approx_abs.py
# ---------------------------------------------------------------------------
#
# ---------------------------------------------------------------------------
from math import pi, cos
import numpy as np
import matplotlib.pyplot as plt

def abs_approx(x, N):
    """
    Returns float with approximation of |x|.

    Arguments:
    x   -- Float. The value to approximate absolute value of.
    N   -- Integer. Controls summation loop.

    Output:
    y   -- Float.
    """
    sum = 0

    #Calculate sum-part of formula
    for k in range(1, N+1):
        arg  = 2*k - 1
        sum += (cos(arg * x))/(arg**2)

    return pi/2 - (4/pi)*sum #Approximation of absolute value


#Variables given in excercise
N = [1, 2, 3, 4]
X = np.linspace(-pi, pi, 101)   #interval [-pi, pi]
exact  = np.absolute(X)
approx = []

#Calculate approximations
y = np.zeros(len(X))            #Temp storage of approximations
for k in N:
    for x in range(len(X)):     #Approximations for all x in X
        y[x] = abs_approx(X[x], k)
    approx.append(y)


#Plot the results vs exact absolute value
fig, axs = plt.subplots(2, 2)
#N=1
axs[0,0].plot(X, approx[0], 'g', label='Approximation')
axs[0,0].plot(X, exact, 'tab:orange', label='Exact')
axs[0,0].set_title('N = 1')
axs[0,0].legend(loc='upper center')
#N=2
axs[0,1].plot(X, approx[1], 'g', label='Approximation')
axs[0,1].plot(X, exact, 'tab:orange', label='Exact')
axs[0,1].set_title('N = 2')
axs[0,1].legend(loc='upper center')
#N=3
axs[1,0].plot(X, approx[2], 'g', label='Approximation')
axs[1,0].plot(X, exact, 'tab:orange', label='Exact')
axs[1,0].set_title('N = 3')
axs[1,0].legend(loc='upper center')
#N=4
axs[1,1].plot(X, approx[3], 'g', label='Approximation')
axs[1,1].plot(X, exact, 'tab:orange', label='Exact')
axs[1,1].set_title('N = 4')
axs[1,1].legend(loc='upper center')
#Label axis and declutter
for box in axs.flat:
    box.set(xlabel='x = [-pi, pi]', ylabel = 'f(x) = |x|')
    box.label_outer() #Remove inner labels

plt.show()


"""
Example:
>>>python3 approx_abs.py
~/IN1900/approx_abs.py:48: MatplotlibDeprecationWarning: The resize_event function
was deprecated in Matplotlib 3.6 and will be removed two minor releases later.
Use callbacks.process('resize_event', ResizeEvent(...)) instead.
  fig, axs = plt.subplots(2, 2)


***And plot displayed in seperate window***

"""
