import numpy as np
import pandas as pd

#dataframe
data  = {
    'Category' : ['A' , 'B' , 'A' , 'B' , 'A' , 'B' , 'A' , 'B'],
    'Store' : ['S1' , 'S1' , 'S2' , 'S2' , 'S1' , 'S2' , 'S2' , 'S1'],
    'Sales' : [100 , 200 , 150 , 250 , 120 , 180 , 200 , 300],
    'Quantity' : [10 , 15 , 12 , 18 , 8 , 20 , 15 , 25],
    'Date' : pd.date_range('2023-01-01' , periods = 8)
}

df = pd.DataFrame(data)
print(df)

print("\n")

#GroupBy

category_sale = df.groupby("Category")["Sales"].sum()
print("=== Category Total sales ===\n")
print(category_sale)

print("\n")

store_sale = df.groupby("Store")["Sales"].sum()
print("=== Store Total sales ===\n")
print(store_sale)

print("\n")

cat_sale = df.groupby(["Category" , "Store"])["Sales"].sum()
print("=== Category and store Total sales ===\n")
print(cat_sale)

print("\n")

#Aggregation

print("Mean : ", df['Sales'].mean())
print("Median : ", df['Sales'].median())
print("Mode : ", df['Sales'].mode())
print("Max : ", df['Sales'].max())
