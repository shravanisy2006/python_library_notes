#importing pandas and numpy

import pandas as pd
import numpy as np

#creating series with dictionary
d = {"a" : 10, "b" : 20, "c" : 30}

dic_series = pd.Series(d)
print("=== Series with Dictionary ===")
print(dic_series)

print("\n")

#creating series with list
l = [10 , 20 , 30]
label = ['Mukesh' , 'Ram' , 'Bob']

list_series = pd.Series(l , label)
print("=== Series with list ===")
print(list_series)

print("\n")

#creating series with array
a = np.array([100 , 200 , 300 , 400])
label_array = ['Science' , 'Maths' , 'English' , 'Hindi']

array_series= pd.Series(a , label_array)
print("=== Series with Array===")
print(array_series)
