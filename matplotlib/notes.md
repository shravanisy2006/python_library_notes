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
