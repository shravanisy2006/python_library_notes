import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

sns.lmplot(tips, x = 'total_bill' , y = 'tip')
plt.show()