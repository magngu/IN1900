# UiO // IN1900 - Introduction to Programming with Scientific Applications
Repository for my [IN1900](https://www.uio.no/studier/emner/matnat/ifi/IN1900/index-eng.html)
excercise solutions and related documents. Readme is primarily a personal note of course contents
and things which should be committed to memory.

![](https://img.shields.io/badge/UiO-IN1900-blueviolet)  ![](https://img.shields.io/badge/Python-Numpy-blueviolet)  ![](https://img.shields.io/badge/Python-MatplotLib-blueviolet)

### Course Overview & Key Points
<details>
  <summary>Python modules used</summary>

  * Math // Cmath // MatplotLib.pyplot // Numpy // Sys

  * Know how to make and import modules
  * Know how to edit where python looks for modules

</details>

<details>
  <summary>Built in data structures</summary>

  * Lists
  * Dictionary
  * Tuple
  * Set

</details>

<details>
  <summary>Working with strings</summary>

  * F-string formatting
  * Format specifiers
  * print()

  ```python
  # f-string formatting
  print(f'Evaluate {variable} at runtime')

  # format specifieer
  print(f'Set space for output {x:8.2f}.')
  ```

</details>


<details>
  <summary>Working with files</summary>

  * [with] statement
  * [.close()](https://docs.python.org/3/tutorial/inputoutput.html)
  * [open()](https://docs.python.org/3/tutorial/inputoutput.html)
  * [write()](https://docs.python.org/3/tutorial/inputoutput.html)
  * [.read()](https://docs.python.org/3/tutorial/inputoutput.html)
  * [.readline()](https://docs.python.org/3/tutorial/inputoutput.html)
  * [.readlines()](https://docs.python.org/3/tutorial/inputoutput.html)

</details>


<details>
  <summary>Lists</summary>

  * Lists are mutable
  * List comprehension
  * List slicing
  * .append()
  * .split()
  * len()

  ```python
    # List comprehension
    # new_list = = [expression for element in iterable]
    my_list = [x**2 for x in range(10)]

  ```

</details>


<details>
  <summary>Loops</summary>

  * While-loop
  * For-loop
  * Mathematical sum as for-loop
  * Break statement
  * Continue statement

</details>


<details>
  <summary>Built in functions</summary>

  * eval()
  * exec()
  * exit()
  * input()
  * len()
  * range()
  * map()
  * open()
  * print()
  * write()
  * zip()

</details>


<details>
  <summary>Exception handling</summary>

  * try-except-finally
  * raise

</details>

<details>
  <summary>Numpy</summary>

  * np.empty()
  * np.linspace()
  * np.mean()
  * np.max()
  * np.min()
  * np.zeros()

  ```python
    # Standard import format
    import numpy as np

  ```

</details>