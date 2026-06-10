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

# Array Reshaping

1. Changing the shape of the Array:

    There are 3 three ways through which we can change the shape of the array.

    - .ravel() : returns the array flatened. 

    - .reshape() : returns the array with the modeified shape.

    - .T : returns the array transposed 

                and 

       .T.shape : returns the shape of the transposed array

---

# Stacking Together Different Arrays

There are different ways through which we can concaneate or stack different arrays:

1. .vstack : stacks array vertically (top to bottom)

2. .hstack : stacks array horizontally (left to right)

3. .r_ : appends elements 

4. .c_ : concatenates two arrays top to bottom

---

# Splitting of Arrays

1. .hsplit - splits array horizontally

    - .hsplit(a, 3) : splits array a into 3 different arrays

    - .hsplit(a, (3, 4)) : splits array a after the 3rd and the 4th column

2. .vplit - splits array vertically

---

# Copies and Views

1. No copy at all

-  Simple assignments make no copy of objects or their data.

2. View or shallow copy (.view)

-  Different array objects can share the same data. The view method creates a new array object that looks at the same data.

-  That is changes in one can also result into changes into other also. They have the same data in their memory.

-  e.g. a = ([1 , 2 , 3 , 4])
        b = a.view()    #Now b is a view of a so any changes made in array a will result in changes in a too

3.  Deep copy

-   The copy method makes a complete copy of the array and its data.

-   Changes in one doesnt reflect in the other.

---

# Functions and Methods overview

1. Array creation:

 arange, array, copy, empty, empty_like, eye, fromfile, fromfunction, identity, linspace, logspace, mgrid, ogrid, ones, ones_like, r_, zeros, zeros_like

2. Conversions :

ndarray.astype, atleast_1d, atleast_2d, atleast_3d, mat
 
3. Manipulations :

array_split, column_stack, concatenate, diagonal, dsplit, dstack, hsplit, hstack, ndarray.item, newaxis, ravel, repeat, reshape, resize, squeeze, swapaxes, take, transpose, vsplit, vstack
 
4. Questions :

all, any, nonzero, where

5. Ordering :

argmax, argmin, argsort, max, min, ptp, searchsorted, sort

6. Operations : 

choose, compress, cumprod, cumsum, inner, ndarray.fill, imag, prod, put, putmask, real, sum

7. Basic Statistics :

cov, mean, std, var

8. Basic Linear Algebra :

cross, dot, outer, linalg.svd, vdot

---

# Broadcasting Rules

Rule No. 1 : If input arrays do not have the same number of dimensions then 1 is added till the time the dimensions aren't the same. 

 Rule No. 2 : Arrays with a size of 1 along a particular dimension act as if they had the size of the array with the largest shape along that dimension. 

 ---

 