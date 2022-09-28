# Created by    : magngul@math.uio.no
# Created date  : 01. sep 2022
# Course        : UiO IN1900
# Excercise     : 3.11 alkane.py
# ---------------------------------------------------------------------------
# Computes molar mass of alkanes with n Carbom atoms and prints it
# ---------------------------------------------------------------------------

Mc = 12.011 #Carbon g/mol
Mh = 1.0079 #Hydrogen g/mol
N  = [i for i in range(2, 10)]  #Number of carbon atoms

#Calculates molar mass and prints result
for n in N:
    m = n*Mc + (2*n+2)*Mh   #Alkane molar mass
    print(f'M(C{n}H{2*n+2}) = {m:.3f} g/mol')


"""
Example:
>>>python3 alkane.py
M(C2H6) = 30.069 g/mol
M(C3H8) = 44.096 g/mol
M(C4H10) = 58.123 g/mol
M(C5H12) = 72.150 g/mol
M(C6H14) = 86.177 g/mol
M(C7H16) = 100.203 g/mol
M(C8H18) = 114.230 g/mol
M(C9H20) = 128.257 g/mol
"""
