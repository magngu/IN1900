# Created by    : Magnus Gullien
# Created date  : 31. aug 2022
# Course        : UiO IN1900
# Excercise     : 3.8 population_table2.py
# ------------------------------------------------------------------------------
# Computes population P(t) and prints table using nested lists
# ------------------------------------------------------------------------------
from math import exp

n  = 12
dt = 48/(n+1)   #Interval length, hours
P  = lambda t: 50000 / (1 + 9*exp(-0.2*t)) #Growth formula, taken from ex 2.3

#Calculates t and N and stores result in two lists
t = []
N = []
for i in range(n+1):
    t.append(i*dt)
    N.append(P(t[i]))

# EXCERCISE PART A--------------------------------------------------------------
#Stores t and N in a nested list
tN1 = [[], []]
tN1[0], tN1[1] = t, N


# EXCERCISE PART B--------------------------------------------------------------
#Stores t[i] and N[i] as paired elements in a list
tN2 = []
for el in zip(t, N):        #Loops over concatination of t & N
    tN2.append(list(el))    #Converts tuple to list, then appends


# PRINTS A & B TOGETHER---------------------------------------------------------
#Table header
print('|---------------------------------------|')
print('|POPULATION TABLE a| |POPULATION TABLE b|')
print('|------------------| |------------------|')
print('|    t   |   N(t)  | |    t  |   N(t)   |')
print('|------------------| |------------------|')

#Populates table with results
for i in range(len(tN1[0])):
    print(f'| {tN1[0][i]:4.0f}   | {tN1[1][i]:6.0f}  | | {tN2[i][0]:4.0f}  |  {tN2[i][1]:6.0f}  |') #t and associated N from tN1
print('|---------------------------------------|')
print('|Note. Numbers rounded to closest int.  |')
print('|---------------------------------------|')


"""
Example:
>>> python3 population_table2.py
|---------------------------------------|
|POPULATION TABLE a| |POPULATION TABLE b|
|------------------| |------------------|
|    t   |   N(t)  | |    t  |   N(t)   |
|------------------| |------------------|
|    0   |   5000  | |    0  |    5000  |
|    4   |   9433  | |    4  |    9433  |
|    7   |  16366  | |    7  |   16366  |
|   11   |  25227  | |   11  |   25227  |
|   15   |  34031  | |   15  |   34031  |
|   18   |  40842  | |   18  |   40842  |
|   22   |  45161  | |   22  |   45161  |
|   26   |  47565  | |   26  |   47565  |
|   30   |  48806  | |   30  |   48806  |
|   33   |  49422  | |   33  |   49422  |
|   37   |  49722  | |   37  |   49722  |
|   41   |  49867  | |   41  |   49867  |
|   44   |  49936  | |   44  |   49936  |
|---------------------------------------|
|Note. Numbers rounded to closest int.  |
|---------------------------------------|
>>>
"""
