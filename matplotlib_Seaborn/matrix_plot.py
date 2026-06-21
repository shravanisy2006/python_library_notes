import matplotlib.pyplot as plt
import seaborn as sns

flights = sns.load_dataset('flights')
tips = sns.load_dataset('tips')

#correlation
correlation = tips [['total_bill' , 'tip' , 'size']].corr()

#heatmap
heat = sns.heatmap(correlation, annot= True , cmap = 'coolwarm')
heat.figure.suptitle("correlation in tips dataset")
plt.tight_layout()
plt.savefig("heatmap.png")
plt.show()

#clutermap

cluster = sns.clustermap(correlation )
cluster.figure.suptitle("correlation in tips dataset")
plt.savefig("clustermap.png")
plt.show()

#pivot table heat map

flight_pivot = flights.pivot_table(values = 'passengers' , index = 'month' , columns = 'year' )
map = sns.heatmap(flight_pivot)
map.figure.suptitle("correlation is flight dataset")
plt.savefig("pivot heat map.png")
plt.show()