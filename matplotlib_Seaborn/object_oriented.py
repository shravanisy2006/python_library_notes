#importing libraries

import matplotlib.pyplot as plt

x = [1 , 2 , 3 , 4 , 5]
y = [2 , 4 , 6 , 8 , 10]

#plotting single graph
fig = plt.figure()
axes = fig.add_axes([0.1 , 0.1 , 0.8 , 0.8])
axes.plot(x , y )
axes.set_title('Double Numbers')
axes.set_xlabel('Numbers')
axes.set_ylabel('Doubled Values')
axes.grid(True)

#plotting graphs with positioning

axes1 = fig.add_axes([0.3 , 0.3 , 0.4 , 0.4])
axes1.plot(x , y)
axes1.set_title('Double Numbers')
axes1.set_xlabel('Numbers')
axes1.set_ylabel('Doubled Values')
axes1.grid(True)

plt.savefig('object_oriented.png')
plt.show()