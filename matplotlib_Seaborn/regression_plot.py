import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

reg = sns.lmplot(tips, x = 'total_bill' , y = 'tip')
reg.figure.suptitle("Prediction of tips wrt total bill")
plt.xlabel("total_bill")
plt.ylabel("tip")
plt.savefig("regression.png")
plt.show()