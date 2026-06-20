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

