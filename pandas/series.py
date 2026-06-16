#importing pandas and numpy
import pandas as pd
import numpy as np

#creating series with dictionary
d = {"a" : 10, "b" : 20, "c" : 30}

ser = pd.Series(data = d, index  = ['a' , 'b' , 'c', ])
print(ser)

#creating series with list
l = [10 , 20 , 30]

seri = pd.Series(data = l )
print(seri)

#creating series witj array
a = np.array([100 , 200 , 300 , 400])

serie = pd.Series(data = a)
print(serie)