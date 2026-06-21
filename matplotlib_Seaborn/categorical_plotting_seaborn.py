#importing libraries
import seaborn as sns
import matplotlib.pyplot as plt

#importing the tips dataset
tips = sns.load_dataset('tips')

# #count plot

# count = sns.countplot(tips, x = 'smoker' , hue = 'sex')
# count.figure.suptitle("Smoker Distribution by Gender")
# plt.xlabel("Smoker")
# plt.ylabel("Count")
# plt.tight_layout()
# plt.savefig('count_plot.png')
# plt.show()

# #bar plot

# bar = sns.barplot(tips, x = 'sex' , y = 'tip' )
# bar.figure.suptitle("Average Tip by Gender")
# plt.xlabel("Gender")
# plt.ylabel("Average Tip")
# plt.tight_layout()
# plt.savefig('bar_plot.png')
# plt.show()

# #box plot

# box = sns.boxplot(tips, x = 'total_bill' , y = 'smoker' , hue = 'sex' )
# box.figure.suptitle("Total Bill Distribution")
# plt.xlabel("Total Bill")
# plt.ylabel("Smoker")
# plt.tight_layout()
# plt.savefig('box_plot.png')
# plt.show()

# #violin plot

# violin = sns.violinplot(tips, x = 'tip' , y = 'sex' , hue = 'smoker' , palette = 'rainbow')
# violin.figure.suptitle("Tip distribution wrt sex")
# plt.xlabel('Tip')
# plt.ylabel('Sex')
# plt.tight_layout()
# plt.savefig("violin_plot.png")
# plt.show()

#strip plpt

strip = sns.stripplot(tips, x = 'day' , y = 'tip' )
strip.figure.suptitle("Tip distribution per day")
plt.xlabel("day")
plt.ylabel("tip")
plt.tight_layout()
plt.savefig("strip_plot.png")
plt.show()