#importing libraries

import matplotlib.pyplot as plt
import numpy as np

#values for x and y axis
x = np.linspace(0 , 5 , 11)
y = x ** 2

#plotting the single line graph
plt.plot(x , y)
plt.title('Squared Numbers')
plt.xlabel('Numbers')
plt.ylabel('Squared Values')
plt.grid(True)
plt.tight_layout()
plt.savefig('images/single_plot.png')
plt.show()

#plotting multiple graphs
plt.subplot (2 , 2 , 1)
plt.title('Squared Numbers')
plt.plot(x , y)

plt.subplot (2 , 2 , 2)
plt.title('Cubed Numbers')
plt.plot(x , x**3)

plt.subplot (2 , 2 , 3)
plt.title('Quartic Numbers')
plt.plot(x , x ** 4)


plt.subplot (2 , 2 , 4)
plt.title('Sine Wave')
plt.plot(x , np.sin(x))

plt.tight_layout()
plt.savefig('multiple_plots.png')
plt.show()

#comparing graphs

x = [1 , 2 , 3 , 4 , 5]

y1 = [1 , 4 , 9 , 16 , 25]
y2 = [1 , 8 , 27 , 64 , 125]

plt.figure(figsize = (6 , 5))

plt.plot(x , y1 , label = 'square')
plt.plot(x , y2 , label = 'cube')

plt.title("Multiple lines plotting")
plt.xlabel("Numbers")
plt.ylabel("Values")
plt.legend()
plt.tight_layout()
plt.savefig("multiple_line_plot.png")
plt.show()