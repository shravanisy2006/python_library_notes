import pandas as pd
import numpy as np

#creating a dataframe with dictionary

d = {
    'Name' : ['John' , 'Alex' , 'Bob'],
    'Age' : [22 , 21 , 24],
    'City' : ['Pune' , 'Banglore' , 'Mumbai'],
    'Salary' : [25000 , 22000 , 21000]
}

dict_dataframe = pd.DataFrame(d)
print("=== Dataframe from Dictionary ===")
print(dict_dataframe)

print("\n")

#creating a dataframe with list

l = [
    ['John' , 22 , 'Pune' , 25000],
    ['Alex' , 21 , 'Banglore' , 22000],
    ['Bob' , 24 , 'Mumbai' , 21000]
]

columns = ["Name" , "Age" , "City" , "Salary"]

label = [1 , 2 , 3]
list_dataframe = pd.DataFrame(l , label, columns)
print("=== Dataframe from list ===")
print(list_dataframe)

print("\n")

#creating a dataframe with array

arr = np.array([
    [1 , 2 , 3],
    [4 , 5 , 6],
    [7 , 8 , 9]
])

column = ['a' , 'b' , 'c']
label = [1 , 2 , 3]

array_dataframe = pd.DataFrame(arr, label , columns = column)
print("=== Dataframe from Array ===")
print(array_dataframe)