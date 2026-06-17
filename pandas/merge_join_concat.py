import numpy as np
import pandas as pd

#Merges

#DataFrames
employee = pd.DataFrame({
    "Employee_id" : [1 , 2 , 3 , 4 ,5],
    "Employee_name" : ['Bob' , 'Max' , 'Anthony' , 'Peter' , 'Linda'],
    "Department" : ['HR' , 'IT' , 'Finance' , 'IT' , 'HR']
} , index = [1 , 2 , 3 , 4 , 5])

salaries = pd.DataFrame({
    "Employee_id" : [1 , 2 , 3 , 6 , 7],
    "Salary" : [60000 , 80000 , 65000 , 70000 , 90000],
    "Bonus" : [5000 , 10000 , 7000 , 8000 , 12000]
}, index = [1 , 2 , 3 , 4 , 5])
 
print(employee)
print("\n")
print(salaries)

print("\n")

#Inner merge
print("=== Inner Merge of both dataframes===\n")
merge_inner = pd.merge(employee , salaries, 'inner')
print(merge_inner)

print("\n")

#outer merge
print("=== Outer Merge of both dataframes===\n")
merge_outer = pd.merge(employee , salaries, 'outer')
print(merge_outer)

print("\n")

#left merge
print("=== left Merge of both dataframes===\n")
merge_left = pd.merge(employee , salaries, 'left')
print(merge_left)

print("\n")

#right merge 
print("=== Right Merge of both dataframes===\n")
merge_right = pd.merge(employee , salaries, 'right')
print(merge_right)

print("\n")

#Concatination

#DataFrames
df1 = pd.DataFrame({
    'A' : ['A0' , 'A1' , 'A2'],
    'B' : ['B0' , 'B1' , 'B2'],
    'C' : ['C0' , 'C1' , 'C2']
})

df2 = pd.DataFrame({
    'A' : ['A3' , 'A4' , 'A5'],
    'B' : ['B3' , 'B4' , 'B5'],
    'C' : ['C3' , 'C4' , 'C5']
})

print(df1)
print("\n")
print(df2)

print("\n")

#inner concatinate
conc_inner = pd.concat([df1 , df2] , join='inner')
print("=== Inner Concatination===\n")
print(conc_inner)

print("\n")

#Joining

#Dataframes
df3 = pd.DataFrame({
    'name' : ['Alice' , 'Bob' , 'charlie']
} , index = [1 , 2 , 3])

df4 = pd.DataFrame({
    'score' : [85 , 90 ,76]
}, index = [2 , 3 , 4])

print(df3)
print("\n")
print(df4)

print("\n")

#left join
print("=== left Join ===\n")
print(df3.join(df4))

print("\n")

#outer join
print("=== Outer Join ===\n")
outer_join = df3.join(df4, how = 'outer')
print(outer_join)