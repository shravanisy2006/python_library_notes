import numpy as np

#indexing
#        0   1   2   3   4   5   6
arr = ([1 , 31 , 6 , 4 , 2 , 9 , 56 ])
print(arr[3])

#slicing
print(arr[2:4:1])

#iterating in one dimensional
for i in arr:
    print(i)

#iterating in two dimensional
a = np.array([[1 , 2 , 3 , 4] , [5 , 6 , 7 , 8],
              [9 , 10 , 11 , 12] , [13 , 14 , 15 , 16]])
# print(a)

#iterating row wise
for row in a:
    print(row)

#iterating for each element
for i in a.flat:
    print(i)

#slicing
print (a[:3:2])  #starts from index row 0 to index row 3 (not including 3) with a gap of 2 rows

#indexing
print(a[2][1]) #10

