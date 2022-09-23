# Created by    : magngul@math.uio.no
# Created date  : 22. sep 2022
# Course        : UiO IN1900
# Excercise     : 5.10 temp_read_write.py
# ------------------------------------------------------------------------------
# Extracts temperatures from file, prints it in terminal and file
# ------------------------------------------------------------------------------
import numpy as np

def extract_data(filename):
    """
    Extracts temperatures for given month from the input file.

    Args:
        filename: string
    """
    temps = []
    with open(filename, 'r') as file:
        file.readline()             #skip header
        temp = file.read().split()  #All values into list as strings
        for el in temp:
            temps.append(float(el))

    return temps


def header():
    """Returns string with header of table"""
    string = ('|----------------------------------|\n'
           +  '| Month    |  Mean |  Max  |  Min  |\n'
           +  '|----------------------------------|'
           )

    return string


def footer():
    """Returns string with footer of table"""
    string = ('|----------------------------------|\n'
           +  '| Note. Temperatures in Celsius    |\n'
           +  '|----------------------------------|'
           )

    return string


def write_formatting(filename, list1, list2):
    """
    Writes data from the two lists to a file. Will overwrite any file with
    identical filename.s

    Args:
        filename:   string. Name of file to be written
        list1:      list. List with temperatures
        list2:      list. Lsit with temperatures

    """
    with open(filename, 'w') as file:
        file.write('|      List1     |       List2     |\n')
        file.write('|----------------------------------|\n')
        for temp1, temp2 in zip(list1, list2):
            file.write(f'| {temp1:10.2f}     | {temp2:10.2f}      |\n')
        file.write(footer())


#-------------------------------------------------------------------------------
oct_1945 = extract_data('temp_oct_1945.txt')
oct_2014 = extract_data('temp_oct_2014.txt')

#Calculate average
mean_1945 = np.mean(oct_1945)
mean_2014 = np.mean(oct_2014)

#Calculate maximum
max_1945 = np.max(oct_1945)
max_2014 = np.max(oct_2014)

#Calculate minimum
min_1945 = np.min(oct_1945)
min_2014 = np.min(oct_2014)

#Print results in a table
print(header())
print(f'| OCT 1945 | {mean_1945:5.2f} | {max_1945:5.2f} | {min_1945:5.2f} |')
print(f'| OCT 2014 | {mean_2014:5.2f} | {max_2014:5.2f} | {min_2014:5.2f} |')
print(footer())

#Write lists to file
write_formatting('temp_formatted.txt', oct_1945, oct_2014)


"""
Example:
>>>python3 temp_read_write.py
|----------------------------------|
| Month    |  Mean |  Max  |  Min  |
|----------------------------------|
| OCT 1945 |  6.51 | 11.60 |  2.10 |
| OCT 2014 |  8.85 | 13.60 |  2.30 |
|----------------------------------|
| Note. Temperatures in Celsius    |
|----------------------------------|


Contents of temps_formatted.txt:
|      List1     |       List2     |
|----------------------------------|
|       7.20     |       9.80      |
|       8.10     |      11.60      |
|       8.90     |      11.50      |
|      11.60     |      13.30      |
|       7.70     |      12.60      |
|       8.70     |      10.30      |
|       6.90     |       7.50      |
|       5.40     |       9.30      |
|       8.80     |      10.30      |
|       8.90     |      10.30      |
|       3.70     |       8.40      |
|       3.30     |       8.80      |
|       5.20     |       5.00      |
|       9.60     |       5.80      |
|      10.80     |       6.80      |
|       5.00     |       2.30      |
|       5.40     |       3.50      |
|       9.50     |       7.90      |
|       5.30     |      11.80      |
|       5.80     |      10.70      |
|       2.30     |       9.00      |
|       4.10     |       5.80      |
|       6.60     |       6.80      |
|       8.20     |      11.70      |
|       6.10     |      10.60      |
|       8.90     |      11.70      |
|       6.60     |      13.10      |
|       4.10     |      13.60      |
|       2.80     |       8.00      |
|       2.10     |       3.50      |
|       4.10     |       3.20      |
|----------------------------------|
| Note. Temperatures in Celsius    |
|----------------------------------|
"""
