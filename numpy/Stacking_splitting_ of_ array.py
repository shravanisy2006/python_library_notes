import numpy as np
import random

## STACKING OF ARRAY

rg = np.random.default_rng()

a = np.floor(10 * rg.random((2, 2)))  
#rg.random((2,2)) generates a 2 by 2 matrix between 0 to 1
#10 * rg.random((2,2)) multiplies by 10 and gives the elements between 1 to 10
#floor rounds off the elements to the nearest whole numbers 
print(a)

print("\n")

b = np.floor(10 * rg.random((2 , 2)))
print(b)

print("\n")

#stacks two arrays vertically i.e. top to bottom
print(np.vstack((a , b)))

print("\n")

#stacks two arrays horizontally i.e. left to right
print(np.hstack((a , b)))

print("\n")

#.r_ prints row wise from 1 to 3 then appends 5 and 6
b = np.r_[1:4 , 5 , 6]
print(b)

print("\n")

#.c_ prints column wise i.e top to bottom first 1,2,3 then downside 4,5,6
c = np.c_[np.array([1 , 2 , 3]) , np.array([4 , 5 , 6])]
print(c)


## SPLITTING OF ARRAY