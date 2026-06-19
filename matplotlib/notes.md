## Matplotlib – Beginner Notes 

## What is Matplotlib?

Matplotlib is a portmanteau of MATLAB, plot, and library. It is a foundational, open-source data visualization library for the Python programming language and its numerical extension, NumPy.

---

# Importing Matplotlib

import matplotlib.pyplot as plt

---

# Line Plot

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
