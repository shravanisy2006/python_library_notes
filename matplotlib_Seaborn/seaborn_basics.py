import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#load the tips dataset

tips = sns.load_dataset('tips')
print(tips)

print(tips.size)
print(tips['size'].unique())
print(tips.shape)

plt.subplot(1 , 2 , 1)
sns.histplot(tips['total_bill'] , kde = True)
plt.subplot(1 , 2 , 2)
sns.histplot(tips['tip'] , kde = True)
plt.tight_layout()
plt.show()