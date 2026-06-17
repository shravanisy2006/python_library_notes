import numpy as np
import pandas as pd

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

print("=== Inner Merge of both dataframes===\n")
merge_inner = pd.merge(employee , salaries, 'inner')
print(merge_inner)

print("\n")

print("=== Outer Merge of both dataframes===\n")
merge_outer = pd.merge(employee , salaries, 'outer')
print(merge_outer)

print("\n")

print("=== left Merge of both dataframes===\n")
merge_left = pd.merge(employee , salaries, 'left')
print(merge_left)

print("\n")

print("=== Right Merge of both dataframes===\n")
merge_right = pd.merge(employee , salaries, 'right')
print(merge_right)

print("\n")

