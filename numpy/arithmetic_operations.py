import numpy as np

a = np.array([10 , 20 , 30 , 40])
b = np.arange(4)

#addition
print(a + b)

#subtraction
print(a - b)

#multiplication
print(a * b)

#matrix multiplication
print(a @ b) 
print(a .dot (b))

#squaring
print(b ** 2)

#indexing
#        0   1   2   3   4   5   6
arr = ([1 , 31 , 6 , 4 , 2 , 9 , 56 ])
print(arr[3])

#slicing
print(arr[2:4:1])

#iterating
for i in arr:
    print(i)
