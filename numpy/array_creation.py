#import numpy
import numpy as np

#Properties of an Array

n = np.array([[[5 , 8 , 2 , 19] , [2 , 28 , 73 , 28]] ,
              [[7 , 32 , 24 , 84] , [2 , 4, 34 , 53]]])

print(n.ndim)  #prints the dimension of the array
print(n.shape) #prints the shape of the array i.e. no. of rows, no. of columns
print(n.size)  #prints the number of elements i.e. no. of  (rows * columns)
print(n.dtype) #prints the type of data an array have

#One Dimensional Array

#create an array
a = np.array([1 , 2 , 3 , 4])
b = np.array([1.2 , 3.4 , 2.7 , 5.3])

#print an array
print(a) 
print(b)

#prints the type of data in the array
print(a.dtype)
print(b.dtype)

#Two Dimensional Array

c = np.array([(1 , 2 , 3) ,
     (4, 5 , 6)])
print(c)
print(c.dtype)

#zero arrays (zeros functions create an array with all elements as 0)

d = np.zeros((4,5))
print(d)

#ones arrays (ones functions create an array with all elements as 1)

e = np.ones((3,2))
print(e)

f = np.ones((2,3,4))
print(f)

#full array

h = np.full((4,4),2)
print(h)

#array with range func

g = np.arange(5 , 30  , 5)  #start from 5 till 30 with gap of 5
print(g)

#random array

random = np.random.random((2,3))
print(random)