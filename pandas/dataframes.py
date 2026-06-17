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

print("\n")

#selection in dataframe

#one column
one_column = list_dataframe['Name']
print("=== Names from the data ===\n")
print(one_column)

print("\n")

#two column
two_column = list_dataframe[['Name', 'City']]
print("=== Names and Cities from the data ===\n")
print(two_column)

print("\n")

#Creating of a new column

list_dataframe["Designation"] = ["Head" , "Manager" , "Lead"]
print("=== New Column ===\n")
print(list_dataframe)

print("\n")

#Removing a Column temprorily

remove_age = list_dataframe.drop("Age" , axis = 1)
print("=== Column Deleted ===\n")
print(remove_age)

print("\n")

#Removing a column permanantly

print(list_dataframe)
print("\n")

rem_age = list_dataframe.drop("Age" , axis = 1 , inplace = True)
print("=== Column Deleted ===\n")
print(rem_age)

print("\n")

#selecting first 2 rows

first_rows = list_dataframe.head(2)
print("=== First 2 rows ===\n")
print(first_rows)

print("\n")

#selecting last 2 rows

last_rows = list_dataframe.tail(2)
print("=== Last 2 rows ===")
print(last_rows)

print("\n")

#targetting specific rows

specific_rows = list_dataframe.loc[1]
print("=== Second Row is ===\n")
print(specific_rows)

print("\n")

#targetting the subsets of rows and colums

subsets = list_dataframe.loc[[1 , 2]][['Name' , 'Salary']]
print("=== Printing the subsets of rows and columns ===\n")
print(subsets)

print("\n")

#targetting based on index

sets1 = list_dataframe.iloc[0]
sets2 = list_dataframe.iloc[0:2, 1:3]
print("=== Targetting based on index value")
print(sets1)
print("\n")
print(sets2)

print("\n")


#conditional selection

condition = list_dataframe[list_dataframe["Salary"] > 24000]
print("=== Conditional selection ===\n")
print(condition)

print("\n")

#multiple conditional statement

mul_condition = list_dataframe[(list_dataframe ["Salary"] > 20000) & (list_dataframe ["City"] == "Banglore")]
print("=== Multiple Conditional selection ===\n")
print(mul_condition)

print("\n")

#sorting

sort = list_dataframe.sort_values(by = 'Salary' ,  axis = 0 , ascending = False)
print("=== Sorted Salary ===\n")
print(sort)

print("\n")

#to fetch info

print("=== Information of dataframe ===\n")
list_dataframe.info()

print("\n")

#statistics description

print("=== Description ===\n")
des = list_dataframe.describe()
print(des) 

print("\n")
