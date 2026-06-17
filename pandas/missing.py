import numpy as np
import pandas as pd

d = {
    "Name": ["Alice", "Bob", "Mark"],
    "Marks": [85, np.nan, 90],
    "Roll No.": [np.nan, 12, 25]
}

df = pd.DataFrame(d)
print("=== Dataframe with null values ===\n")
print(df)

print("\n")

#isna
print("=== Dataframe with isna boolean input ===\n")
print(df.isna())
print("\n")
print("=== Dtaframe with total number of null values per row ===\n")
print(df.isna().sum())

print("\n")

#notnull
print("=== Dataframe with notnull boolean input ===\n")
print(df.notnull())

print("\n")

#dropna
print("=== Dataframe with dropper null values ===\n")
print(df.dropna())

print("\n")

#fillna
print("=== Dataframe with null values as none ===\n")
print(df.fillna('None'))

print("\n")

print("=== Dataframe with null values as mean ===\n")
values = {"Name" : 'None' ,
          "Marks" : df["Marks"].mean(),
          "Roll No.": 'Unique'}

print(df.fillna(values))