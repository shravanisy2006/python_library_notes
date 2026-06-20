import seaborn as sns
import matplotlib.pyplot as plt

#load the tips dataset

tips = sns.load_dataset('tips')
print(tips.head(10))

print("\n")

#dataset analysis 

print(tips.size)
print(tips['size'].unique())

print("\n")

tips.info()

print("\n")

print(tips.describe())

#CDistrubution plotting

#hist plot

plt.subplot(1 , 2 , 1)
sns.histplot(tips['total_bill'] , kde = True)
plt.title("Histogram for Total bill")

plt.subplot(1 , 2 , 2)
sns.histplot(tips['tip'] , kde = True)
plt.title("Histogram for Tips")

plt.tight_layout()
plt.savefig("histogram_plot.png")
plt.show()

#joint plot

joint = sns.jointplot(x = 'total_bill' , y = 'tip' , data = tips , kind = 'hist')

joint.figure.suptitle("Comparison Analysis")
joint.figure.subplots_adjust(top=0.95)
plt.tight_layout()
# plt.savefig("histogram_comparison.png")
plt.show()

# pair plot

pair = sns.pairplot(tips , hue = 'size' , palette = 'rainbow')
pair.figure.suptitle('Pair plot' )
plt.tight_layout()
plt.savefig('pait_plot.png')
plt.show()

#rug plot

rug = sns.rugplot(tips, x = 'total_bill' , y = 'tip' , hue = 'size' , palette = 'rainbow')
rug.figure.suptitle('rug plot')
plt.tight_layout()
plt.savefig('rug_plot.png')
plt.show()