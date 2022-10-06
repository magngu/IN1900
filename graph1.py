# Created by    : magngul@math.uio.no
# Created date  : 03. oct 2022
# Course        : UiO IN1900
# Excercise     : 6.14 graph1.py
# ---------------------------------------------------------------------------
# Function plotting complete graph from set of (x,y) coordinates
# ---------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt


def plot_line(p1, p2):
    """Takes two tuples with (x,y) coordinates and plots the line between them"""
    try:
        #Find formula for line
        a = (p2[1] - p1[1]) / (p2[0] - p1[0])   # Slope of line: (y2 - y1) / (x2 - x1)
        f = lambda x: a*x - a*p1[0] + p1[1]     # f(x) = ax - a*x0 + y0 = ax + b

        #Calculate points
        x = np.linspace(p1[0], p2[0], 101)
        y = f(x)

    #Catches if line is vertical
    except ZeroDivisionError:
        x = np.linspace(p1[0], p1[0], 101)  #Constant x
        y = np.linspace(p1[1], p2[1], 101)

    #Plot points
    plt.plot(x,y, 'b')


def complete_graph(points):
    """
    Takes list of points and plots the complete graph of the points.

    Arguments:
    points  -- List. Contains tuples or lists with (x,y) coordinates

    Output:
    Displays plot
    """
    for pt in points:
        pt_indx = points.index(pt)
        nxt_pt  = pt_indx+1

        #Plots lines to points with higher index only
        for i in range(nxt_pt, len(points)):
            plot_line(pt, points[i])

    plt.show()


#EXERCISE PART A - Demonstrate function works
h1, h2 = (2,2), (10,2)
v1, v2 = (2,1), (2,10)

plot_line(h1, h2)
plot_line(v1, v2)
plt.show()

#EXERCISE PART B - Plot complete graphs
a = sqrt(2)/2
points1 = ( (0,0), (1,0), (0,1), (1,1) )
points2 = ( (1,0), (a,a), (0,1), (-a,a), (-1,0), (-a,-a), (0,-1), (a,-a))

complete_graph(points1)
complete_graph(points2)


"""
>>>python3 graph1.py
/IN1900/graph1.py:30: MatplotlibDeprecationWarning: The resize_event function was deprecated in Matplotlib 3.6 and will be removed two minor releases later. Use callbacks.process('resize_event', ResizeEvent(...)) instead.
  plt.plot(x,y, 'b')

***3 plots shown in consecutive order***

"""
