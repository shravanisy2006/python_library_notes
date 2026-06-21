import numpy as np

a = np.array([[1 , 2 , 3 , 4] ,
              [5 , 6 , 7 , 8],
              [9 , 10 , 11 , 12]])


#original shape
print(a.shape) 

#refined shape
print(a.ravel()) #prints all elements flattend

print(a.reshape(6,2)) #prints the reshaped array in the form of 6 by 2

print(a.T.shape) #prints the transposed array shape


#Conversion of 1D Array into 2d Array 


#np.newaxis
a = np.array([1 , 2 , 3 , 4 , 5])
print(a.ndim ,"\n")
print(a.shape)

b = a[np.newaxis , :]
print(b)
print(b.shape)
print(b.ndim)

#np.expand_dims
a = np.array([2 , 4 , 6 , 8])
b = np.expand_dims (a , axis = 1)
print(b)
