# Matplotlib – Beginner Notes 

# What is Matplotlib?

Matplotlib is a portmanteau of MATLAB, plot, and library. It is a foundational, open-source data visualization library for the Python programming language and its numerical extension, NumPy.

---

## Importing Matplotlib

import matplotlib.pyplot as plt

---

## Line Plot

A line plot is used to visualize trends, patterns, and relationships between variables.

Syntax:

```python
plt.plot(x, y)
```

---

## Common Functions

### plt.plot()

Plots points and connects them using a line.

Syntax:

```python
plt.plot(x, y)
```

Parameters:

* x → values for x-axis
* y → values for y-axis

---

### plt.title()

Adds a title to the graph.

Syntax:

```python
plt.title("Graph Title")
```

Example:

```python
plt.title("Squared Numbers")
```

---

### plt.xlabel()

Adds a label to the x-axis.

Syntax:

```python
plt.xlabel("Label Name")
```

Example:

```python
plt.xlabel("Numbers")
```

---

### plt.ylabel()

Adds a label to the y-axis.

Syntax:

```python
plt.ylabel("Label Name")
```

Example:

```python
plt.ylabel("Squared Values")
```

---

### plt.grid()

Displays grid lines on the graph for better readability.

Syntax:

```python
plt.grid(True)
```

or

```python
plt.grid(axis='y')
```

Example:

```python
plt.grid(True)
```

---

### plt.show()

Displays the graph output.

Syntax:

```python
plt.show()
```

Without this function, the graph may not be displayed.

---

### plt.savefig()

Saves the graph as an image file.

Syntax:

```python
plt.savefig("graph.png")
```

Example:

```python
plt.savefig("line_plot.png")
```

---

### plt.tight_layout()

Automatically adjusts spacing between graph elements to avoid overlapping labels and titles.

Syntax:

```python
plt.tight_layout()
```

Recommended before:

```python
plt.savefig()
```

or

```python
plt.show()
```

---

# Subplots

Subplots allow multiple graphs to be displayed within a single figure.

Syntax:

```python
plt.subplot(rows, columns, position)
```

Parameters:

* rows → number of rows
* columns → number of columns
* position → location of graph

Example:

```python
plt.subplot(2, 2, 1)
```

Meaning:

* 2 rows
* 2 columns
* First graph position

Layout:

```text
1 | 2
-----
3 | 4
```
---

# Figure Size

Used to control the width and height of a graph.

Syntax:

```python
plt.figure(figsize=(width, height))
```

Example:

```python
plt.figure(figsize=(8,5))
```

Parameters:

* width → width of figure
* height → height of figure

---

# Common Plot Styles

Matplotlib allows customization of line appearance.

Syntax:

```python
plt.plot(x, y, color='blue', linestyle='--', marker='o')
```

Parameters:

* color → changes line color
* linestyle → changes line style
* marker → adds markers on data points

Common Line Styles:

* '-' → Solid Line
* '--' → Dashed Line
* '-.' → Dash-Dot Line
* ':' → Dotted Line

Common Markers:

* 'o' → Circle
* 's' → Square
* '^' → Triangle
* '*' → Star

---

# Multiple Lines in One Graph

Used to compare multiple datasets in a single graph.

Example:

```python
plt.plot(x, x**2)
plt.plot(x, x**3)
```

---

# plt.legend()

Displays labels for multiple plotted lines.

Syntax:

```python
plt.legend()
```

Example:

```python
plt.plot(x, x**2, label="Square")
plt.plot(x, x**3, label="Cube")

plt.legend()
```

Output:

A small box appears showing:

```text
Square
Cube
```

---

# Order of Plotting Commands

A typical Matplotlib workflow:

```python
plt.figure()

plt.plot()

plt.title()

plt.xlabel()

plt.ylabel()

plt.grid()

plt.legend()

plt.tight_layout()

plt.savefig()

plt.show()
```

Recommended order:

1. Create Figure
2. Plot Data
3. Add Labels
4. Add Grid/Legend
5. Adjust Layout
6. Save Figure
7. Show Figure

---

# Object-Oriented Approach

Matplotlib provides an Object-Oriented (OO) approach where plots are created using Figure and Axes objects.

Advantages:

* More control over plots
* Better for complex visualizations
* Allows multiple plotting areas in one figure

---

## fig.add_axes()

Used to add an Axes object to a Figure.

Syntax:

```python
axes = fig.add_axes([
    left,
    bottom,
    width,
    height
])
```

Parameters:

* left → distance from left side
* bottom → distance from bottom side
* width → width of plotting area
* height → height of plotting area

All values range between 0 and 1.

Example:

```python
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
```

---

## Multiple Axes

Multiple plotting areas can be added within the same figure.

Example:

```python
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])

axes2 = fig.add_axes([0.3, 0.3, 0.4, 0.4])
```

This creates:

* One main graph
* One smaller graph inside the figure

Useful for comparing plots or creating inset visualizations.

---

## Understanding add_axes()

Syntax:

axes = fig.add_axes([left, bottom, width, height])

Example:

axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

Meaning:

- left = 0.1 → 10% from left
- bottom = 0.1 → 10% from bottom
- width = 0.8 → 80% width
- height = 0.8 → 80% height

All values range between 0 and 1.

---

# Types of Plots

# Bar Plot

A bar plot is used to compare values across different categories.

Syntax:

```python
plt.bar(x, y)
```

Parameters:

* x → categories or labels
* y → values

Example:

```python
plt.bar(x, y)
```

Uses:

* Comparing categories
* Sales Analysis
* Student Marks Comparison

---

# Pie Chart

A pie chart represents data as portions of a whole.

Syntax:

```python
plt.pie(data, labels=labels, autopct='%1.1f%%')
```

Parameters:

* data → numerical values
* labels → category labels
* autopct → percentage display format

Example:

```python
plt.pie(y, labels=Labels, autopct='%1.1f%%')
```

Uses:

* Percentage Analysis
* Market Share Visualization
* Category Distribution

---

# Box Plot

A box plot visualizes the spread and distribution of data.

Syntax:

```python
plt.boxplot(data)
```

Example:

```python
plt.boxplot(y)
```

Uses:

* Detecting Outliers
* Understanding Data Spread
* Comparing Distributions

---

## Understanding a Box Plot

A box plot contains:

1. Minimum Value
2. First Quartile (Q1)
3. Median (Q2)
4. Third Quartile (Q3)
5. Maximum Value

Outliers are displayed as separate points outside the whiskers.

---

# Scatter Plot

A scatter plot displays individual data points and is used to analyze relationships between two variables.

Syntax:

```python
plt.scatter(x, y)
```

Parameters:

* x → values for x-axis
* y → values for y-axis

Example:

```python
plt.scatter(x, y)
```

Uses:

* Relationship Analysis
* Trend Detection
* Outlier Detection

---

# Histogram

A histogram is used to visualize the distribution of numerical data.

Syntax:

```python
plt.hist(data, bins=n)
```

Parameters:

* data → numerical dataset
* bins → number of intervals

Example:

```python
plt.hist(y, bins=5)
```

Uses:

* Frequency Analysis
* Data Distribution
* Pattern Detection

---

## Common Histogram Parameters

### bins

Controls the number of intervals.

Example:

```python
plt.hist(data, bins=10)
```

More bins → More detailed distribution

Fewer bins → Simpler distribution

---

# Common Plot Types Summary

| Plot Type    | Purpose                              |
| ------------ | ------------------------------------ |
| Line Plot    | Show trends over time                |
| Bar Plot     | Compare categories                   |
| Scatter Plot | Show relationships between variables |
| Histogram    | Show frequency distribution          |
| Pie Chart    | Show percentage contribution         |
| Box Plot     | Show data spread and outliers        |

---

# Learning Outcomes

Through these notes, I learned:

- Creating and customizing plots
- Working with multiple graphs
- Understanding object-oriented plotting
- Visualizing distributions and relationships
- Saving and exporting graphs
- Comparing different visualization techniques

-----
-----
-----

# Seaborn - Beginner Notes

## What is Seaborn?

Seaborn is a Python data visualization library built on top of Matplotlib. It provides a high-level interface for creating attractive and informative statistical graphics.

### Advantages

- Easy to use
- Built on Matplotlib
- Better default styling
- Statistical visualizations
- Works seamlessly with Pandas DataFrames

---

# Importing Seaborn

```python
import seaborn as sns
import matplotlib.pyplot as plt
```

---

# Built-in Datasets

Seaborn provides built-in datasets for learning and practice.

## Syntax

```python
sns.load_dataset('dataset_name')
```

## Example

```python
tips = sns.load_dataset('tips')
```

---

# Dataset Exploration

## head()

Displays the first *n* rows of a dataset.

### Syntax

```python
dataframe.head(n)
```

### Example

```python
tips.head(10)
```

---

## info()

Displays:

- Column Names
- Data Types
- Non-null Values
- Memory Usage

### Syntax

```python
dataframe.info()
```

### Example

```python
tips.info()
```

---

## describe()

Provides a statistical summary of numerical columns.

### Includes

1. Count
2. Mean
3. Standard Deviation
4. Minimum Value
5. 25th Percentile
6. 50th Percentile (Median)
7. 75th Percentile
8. Maximum Value

### Syntax

```python
dataframe.describe()
```

### Example

```python
tips.describe()
```

---

## unique()

Returns all unique values present in a column.

### Syntax

```python
dataframe['column_name'].unique()
```

### Example

```python
tips['size'].unique()
```

---

# Distribution Plots

Distribution plots help understand how data values are spread.

---

## histplot()

Displays the frequency distribution of numerical data.

### Syntax

```python
sns.histplot(data)
```

### Example

```python
sns.histplot(
    tips['total_bill'],
    kde=True
)
```

### Parameters

| Parameter | Description |
|------------|------------|
| data | Numerical data |
| kde | Displays density curve |

### Uses

- Frequency Analysis
- Distribution Analysis
- Outlier Detection

---

## KDE (Kernel Density Estimation)

Provides a smooth estimate of the data distribution.

### Syntax

```python
sns.histplot(
    data,
    kde=True
)
```

### Example

```python
sns.histplot(
    tips['tip'],
    kde=True
)
```

---

## jointplot()

Displays the relationship between two variables along with their distributions.

### Syntax

```python
sns.jointplot(
    x='column1',
    y='column2',
    data=dataframe
)
```

### Example

```python
sns.jointplot(
    x='total_bill',
    y='tip',
    data=tips,
    kind='hist'
)
```

### Common Types

```python
kind='scatter'
kind='hist'
kind='hex'
kind='kde'
```

### Uses

- Correlation Analysis
- Relationship Visualization
- Bivariate Distribution Analysis

---

## pairplot()

Creates pairwise relationships between numerical features.

### Syntax

```python
sns.pairplot(dataframe)
```

### Example

```python
sns.pairplot(
    tips,
    hue='size',
    palette='rainbow'
)
```

### Parameters

| Parameter | Description |
|------------|------------|
| hue | Grouping variable |
| palette | Color theme |

### Uses

- Feature Relationship Analysis
- Exploratory Data Analysis (EDA)
- Correlation Discovery

---

## rugplot()

Displays each observation as a small tick mark.

### Syntax

```python
sns.rugplot(
    data=dataframe,
    x='column_name'
)
```

### Example

```python
sns.rugplot(
    data=tips,
    x='total_bill'
)
```

### Uses

- Understanding Data Distribution
- Identifying Clusters
- Detecting Data Density

---

# Common Parameters

## hue

Used to add color grouping based on a categorical variable.

### Example

```python
hue='sex'
```

---

## palette

Used to change the color theme of a plot.

### Example

```python
palette='rainbow'
```

### Popular Palettes

```python
deep
muted
bright
pastel
dark
colorblind
rainbow
```

---

# Saving Plots

### Syntax

```python
plt.savefig("image_name.png")
```

### Example

```python
plt.savefig("histogram_plot.png")
```
---

# Categorical Plots

Categorical plots are used to visualize relationships involving categorical variables.

---

## countplot()

Displays the count of observations in each categorical bin.

### Syntax

```python
sns.countplot(
    data=dataframe,
    x='column_name'
)
```

### Example

```python
sns.countplot(
    data=tips,
    x='smoker',
    hue='sex'
)
```

### Uses

- Counting categorical observations
- Comparing category frequencies
- Visualizing class distribution

---

## barplot()

Displays the average value of a numerical variable for each category.

### Syntax

```python
sns.barplot(
    data=dataframe,
    x='categorical_column',
    y='numerical_column'
)
```

### Example

```python
sns.barplot(
    data=tips,
    x='sex',
    y='tip'
)
```

### Uses

- Comparing averages
- Category-wise analysis
- Summarizing data

---

## boxplot()

Visualizes the distribution of numerical data across categories.

### Syntax

```python
sns.boxplot(
    data=dataframe,
    x='categorical_column',
    y='numerical_column'
)
```

### Example

```python
sns.boxplot(
    data=tips,
    x='smoker',
    y='total_bill',
    hue='sex'
)
```

### Uses

- Detecting outliers
- Comparing distributions
- Understanding data spread

---

## violinplot()

Combines a box plot with a density plot.

### Syntax

```python
sns.violinplot(
    data=dataframe,
    x='categorical_column',
    y='numerical_column'
)
```

### Example

```python
sns.violinplot(
    data=tips,
    x='sex',
    y='tip',
    hue='smoker'
)
```

### Uses

- Visualizing distribution shape
- Comparing multiple distributions
- Understanding data density

---

## stripplot()

Displays individual observations for each category.

### Syntax

```python
sns.stripplot(
    data=dataframe,
    x='categorical_column',
    y='numerical_column'
)
```

### Example

```python
sns.stripplot(
    data=tips,
    x='day',
    y='tip'
)
```

### Uses

- Observing individual data points
- Detecting outliers
- Comparing category distributions

---

## swarmplot()

Displays individual observations without overlapping.

### Syntax

```python
sns.swarmplot(
    data=dataframe,
    x='categorical_column',
    y='numerical_column'
)
```

### Example

```python
sns.swarmplot(
    data=tips,
    x='day',
    y='tip'
)
```

### Uses

- Visualizing distributions
- Avoiding overlapping points
- Identifying clusters

---

# Matrix Plots

Matrix plots are used to visualize relationships between multiple variables.

---

## heatmap()

Displays values using color intensity.

### Syntax

```python
sns.heatmap(data)
```

### Example

```python
correlation = tips[
    ['total_bill', 'tip', 'size']
].corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap='coolwarm'
)
```

### Parameters

| Parameter | Description |
|------------|------------|
| annot | Displays values inside cells |
| cmap | Changes color theme |

### Uses

- Correlation Analysis
- Feature Relationship Analysis
- Exploratory Data Analysis

---

## clustermap()

Displays a heatmap with hierarchical clustering.

### Syntax

```python
sns.clustermap(data)
```

### Example

```python
sns.clustermap(
    correlation,
    cmap='coolwarm'
)
```

### Uses

- Feature Similarity Analysis
- Hierarchical Clustering
- Correlation Visualization

---

# Regression Plots

Regression plots help visualize relationships between variables and fit regression lines.

---

## lmplot()

Displays a scatter plot along with a linear regression line.

### Syntax

```python
sns.lmplot(
    data=dataframe,
    x='feature1',
    y='feature2'
)
```

### Example

```python
sns.lmplot(
    data=tips,
    x='total_bill',
    y='tip'
)
```

### Uses

- Trend Detection
- Regression Analysis
- Predictive Analysis
- Relationship Analysis

---

# Updated Common Seaborn Plot Types

| Plot Type | Purpose |
|------------|----------|
| histplot() | Distribution Analysis |
| jointplot() | Relationship Between Two Variables |
| pairplot() | Relationship Between Multiple Variables |
| rugplot() | Individual Data Point Distribution |
| countplot() | Count Category Frequencies |
| barplot() | Compare Category Averages |
| boxplot() | Detect Outliers and Distribution |
| violinplot() | Show Distribution Shape |
| stripplot() | Show Individual Observations |
| swarmplot() | Non-overlapping Observations |
| heatmap() | Correlation Visualization |
| clustermap() | Hierarchical Clustering |
| lmplot() | Regression Analysis |

---

# Learning Outcomes

Through these notes, I learned:

- Creating statistical visualizations
- Exploring categorical data
- Understanding correlations
- Performing regression analysis
- Visualizing relationships between features
- Performing Exploratory Data Analysis (EDA)

---