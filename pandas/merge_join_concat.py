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
