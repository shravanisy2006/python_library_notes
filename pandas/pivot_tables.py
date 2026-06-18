import numpy as np
import pandas as pd 
import random

data = {
    'Date' : pd.date_range('2023-01-01' , periods = 20),
    'Product' : ['A' , 'B' , 'C' , 'D' ] * 5,
    'Region' : ['East' , 'North' , 'West' , 'South'] * 5,
    'Sales' : np.random.randint(100 , 1000 , size = 20),
    'Units' : np.random.randint(10 , 100 , size = 20),
    'Rep' : ['John' , 'Mary' , 'Bob' , 'Alice'] * 5
}

df = pd.DataFrame(data)

df['Month'] = df['Date'].dt.month
df['Quarter']= 'Q' + df['Date'].dt.quarter.astype(str)

print(df)
print("\n")

df1 = pd.pivot_table(df, values = 'Sales' , index = 'Region', columns  = 'Product'  )
print("=== Pivot Table 1 ===\n")
print(df1)

df2 = pd.pivot_table(df, values = ['Sales' , 'Units'] , index = 'Region' , columns = 'Product' , aggfunc = np.sum)
print("=== Pivot Table 2 ===\n")
print(df2)
