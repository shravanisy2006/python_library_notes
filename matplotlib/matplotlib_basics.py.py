#importing libraries

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#values foe=r x and y axis
x = np.linspace(0 , 5 , 11)
y = x ** 2

#plotting the single line graph
plt.plot(x , y)
plt.title('Squared Numbers')
plt.xlabel('Numbers')
plt.ylabel('Squared Values')
plt.grid(True)
plt.tight_layout()
plt.savefig('Single_plot.png')
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