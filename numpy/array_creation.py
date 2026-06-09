#One Dimensional Array

#import numpy
import numpy as np

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

#array with range func

g = np.arange(5 , 30  , 5)  #start from 5 till 30 with gap of 5
print(g)