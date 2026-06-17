## Pandas - Beginner Notes

## What is Pandas?

pandas is a Python package that provides fast, flexible, and expressive data structures designed to make working with “relational” or “labeled” data both easy and intuitive.

The two primary data structures of pandas :
1.  Series (1-dimensional) 
2. DataFrame (2-dimensional)

---

# Series (1-Dimensional)

class pandas.Series(data, index, dtype, name, copy)

Parameters:

- data : array-like, Iterable, dict, or scalar value

- index : array-like or Index (1d)

- dtype : str, numpy.dtype, or ExtensionDtype, optional

- name : Hashable, default None

- copy : bool, default None

Different ways to print series:

- Through dictionary

- Through list

- Through array

---

# DataFrames (2-Dimensional)

class pandas.DataFrame(data, index, columns, dtype, copy)

Parameters: 

- data : ndarray (structured or homogeneous), Iterable, dict, or DataFrame

- index : Index or array-like

- columns : Index or array-like

- dtype : dtype, default None

- copy : bool or None, default None

Different ways to print series:

- Through dictionary

- Through list

- Through array

---

# selection in dataframe

Here index value dont play any role to select a column we have to provide with the name of the column.

syntax : variable_name = name_of_dataframe['column_name']

---

# Creating a new column in dataframe

Here we can directly provide with the new name of column then assigning it a list of inputs.

** Note ** : The number of inputs in list must be equal to the number of inputs in already existing column.

syntax : name_of_dataframe["New_Column_Name"] = [list of inputs]

--- 

# Deleting a column

- First Method

    Deleting a column in a dataframe can be done through drop function.

    syntax : name_of_variable = data_frame_name.drop('column_name' , axis = int)

- Second Method

    Deleting a column in a dataframe can also be done through one of the pramater in drop that is inplace and giving the boolean value as True.

    syntax : name_of_variable = data_frame_name.drop('column_name' , axis = int , inplace = True)

---

## First Method vs Second Method

First method after performing delete operation it just provides with a copy of the dataframe with the deleted column but in second method the column is deleted from the memory itself and if you print the dataframe again in future you wont be able to see the column in it.

---

# Selecting Rows

## Head() , Tail() and .loc[]

- Head(n) : provides with the first n rows

- Tail(n) : provides with the last n rows

- .loc[n] : provides with proper detailed nth row info with column name and its input

---

# Selecting subsets of Rows and Columns

Subsets of rows and columns can be selected using `.loc[]` by specifying row indices and column names simultaneously.

syntax = variable_name = name_of_datafrane.loc[row_index][column_name]

---

# Conditional Selection

Allows you to select a row with applied conditions.

syntax = variable_name = dataframe_name[dataframe_name['column_name_to_apply_condition_on'] condition]

---

# info()

Provides with:

1. RangeIndex

2. Columns

3. Non-null count

4. Data types

5. Memory usage

syntax : name_of_dataframe.info()

---

# describe()

Provides with statistical summary.

1. count

2. mean

3. standard deviation

4. minimum value 

5. 1st quartile

6. 2nd quartile

7. 3rd quartile

8. maximum value 

syntax : variable_name = name_of_dataframe.describe()

---

# Missing Values

1. .isna() : provides boolean value 'True'  where a null value is presented.

    syntax : dataframe_name.isna()

2. .notnull() : provides boolean value 'True' where a value is present and 'False' where a null value is present.

    syntax : dataframe_name.notnull()

3. .dropna() : drope row where a null value is presented.

    syntax : dataframe_name.dropna()

4. .fillna() : replaces null values with a specified value.

    syntax : dataframe_name.fillna(value)

---

# GroupBy

Used to split data into groups and perform aggregate operations.

Common functions:

1. mean()

2. sum()

3. count()

4. max()

5. min()

---

