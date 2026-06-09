## NumPy – Beginner Notes 

## What is NumPy?

NumPy (Numerical Python) is a Python library used for working with numbers and large amounts of data efficiently.

It provides a special data structure called an array, which is faster and more powerful than Python lists for mathematical operations.

Why do we use NumPy?

Faster than normal Python lists

Uses less memory

Easy mathematical calculations

Helpful in Data Science, Machine Learning, and AI

Supports multi-dimensional data (rows, columns, tables)

---

# Installing NumPy

pip install numpy
  
---

# Importing NumPy

import numpy as np

---

# The Basics

1. NumPy's array is called as ndarray also known as array.

2. The more important attributes of an ndarray object are:

    a. ndarray.ndim
    -  the number of axis (dimensions) of the array.

    b. ndarray.shape
    -  the dimensions of the array also a tuple indicating integers for the size of tuple in each dimensions.

    c. ndarray.size
    -  the total number of elements in the array.

---

# Different array function

1. zeros function
-  create an array with all elements as zero.

2. ones function
-  create an array with all elements as one.

3. arange
-  create sequence of array

4. linspace
-  receives an argument for the number of elements an array should have.

---

# Arithmetic Operations on Arrays

Arithmetic operations work element wise on the array.

Arithmetic Multiplication vs Matrix Multiplication

'*' - works element wise 

'@' or '.dot' - performs matix multiplication

# Indexing, slicing and iterating

Indexing : Indexing starts with 0

Slicing : Here we can print only a part of elements or a pattern of elements. Three inputs are given start point , end point and the gap number.

Iterating : Works as a loop and written as (for i in a:)

---

