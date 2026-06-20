#importing libraries

import matplotlib.pyplot as plt

x = [1 , 2 , 3 , 4 , 5]
y = [2 , 4 , 6 , 8 , 10]

#bar plot

plt.bar(x , y)
plt.title('Bar Plot')
plt.xlabel('Numbers')
plt.ylabel('Doubled Values')
plt.grid(True)
plt.savefig('bar_plot.png')
plt.show()

#Pie chart

Labels = ['A' , 'B' , 'C' , 'D' , 'E']
plt.pie(y, labels = Labels, autopct = '%1.1f%%' )
plt.title('Pie Chart')
plt.savefig("pie_chart.png")
plt.show()

#Scatter plot

plt.scatter(x , y)
plt.title('Scatter Plot')
plt.xlabel('Numbers')
plt.ylabel('Doubled Values')
plt.grid(True)
plt.savefig('scatter_plot.png')
plt.show()

#histogram 

plt.hist(y , bins = 5)
plt.title('Histogram')
plt.xlabel('Doubled Values')
plt.ylabel('Frequency')
plt.grid(True)
plt.savefig('histogram.png')
plt.show()

#box plot

plt.boxplot(y)
plt.title('Box Plot')
plt.ylabel('Doubled Values')
plt.grid(True)
plt.savefig('box_plot.png')
plt.show()