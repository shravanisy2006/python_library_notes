import numpy as np
import pandas as pd

d = {
    "Name": ["Alice", "Roy", "Mark", "Sarah", "Jacob"],
    "Department": ["CSE", "IT", "CSE", "IT", "AIDS"],
    "Marks": [85, 78, 92, 88, 70]
}

df = pd.DataFrame(d)
print("=== Dataframe ===\n")
print(df)

print("\n")

marks_distribution = df.groupby("Department")["Marks"].mean()
print("=== Average Marks by Department ===\n")
print(marks_distribution)

print("\n")

highest_marks = df.groupby("Department")["Marks"].max()
print("=== Highest Marks by Department ===\n")
print(highest_marks)

print("\n")

total_marks = df.groupby("Department")["Marks"].sum()
print("=== Total Marks by Department ===\n")
print(total_marks)

print("\n")

student_count = df.groupby("Department")["Name"].count()
print("=== Student count by Department===\n")
print(student_count)

print("\n")

