# Created by    : magngul@math.uio.no
# Created date  : 20. sep 2022
# Course        : UiO IN1900
# Excercise     : 5.7 read_file_isotopes.py
# ------------------------------------------------------------------------------
# Reads file with oxygen isotopes and calculates the molar mass
# ------------------------------------------------------------------------------
"""
Contents of oxygen.txt:
Isotope    weight [g/mol]    Natural abundance
(16)O          15.99491         0.99759
(17)O          16.99913         0.00037
(18)O          17.99916         0.00204
"""

#Extract weight and abundance from file
with open('oxygen.txt', 'r') as file:
    isotopes = []
    file.readline() #skips header
    for line in file:
        isotopes.append(line.split()[1:])#index[0]: weight | index[1]: abundance

#Calculate molar mass
molar = 0
for isotope in isotopes:
    molar += float(isotope[0]) * float(isotope[1]) #weight * abundance

#Print result per excercise specifications
print(f'The molar mass i {molar:.4f} g/mol.')


"""
>>>python3 read_file_isotopes.py
The molar mass i 15.9994 g/mol.
"""
