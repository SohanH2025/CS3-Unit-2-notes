import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



sns.set_theme(style='darkgrid', palette='deep')
#style: darkgrid, whitegrid, dark, white, ticks
#palette: deep, muted, bright, pastel, dark, colorblind

data = np.random.multivariate_normal([0,0], [[5,2], [2,2]], size=2000)
data = pd.DataFrame(data, columns=['x','y'])
for col in 'xy':
    plt.hist(data[col], density=True, alpha=0.5)
plt.savefig('hist.png', bbox_inches='tight')
plt.close()

#kernel densityestimation gices a smoth estimate of deistribution values

sns.kdeplot(data=data, fill=True)
plt.savefig('sns-kdeplotpng', bbox_inches='tight')
plt.close()


iris = sns.load_dataset("iris")
print(iris.head())
sns.pairplot(iris, hue='species', height=2.5)
plt.savefig('sns-pairplot.png')
plt.close()

tips = sns.load_dataset('tips')
print(tips.head())

tips['tip_percent'] = 100 * tips['tip'] / tips['total_bill']

grid = sns.FacetGrid(tips, row='sex', col="time", margin_titles =True)
grid.map(plt.hist, "tip_percent", bins=np.linspace(0,40,15))
plt.savefig('sns-facetgrid.png', bbox_inches='tight')
plt.close()

sns.catplot(x="day", y="total_bill", hue="sex", data=tips, kind="box")
#sns.set_axis_labels("Day", "Total Bill")
plt.savefig("sns-catplot.png", bbox_inches="tight")
plt.close()


sns.jointplot(x='total_bill', y='tip', data=tips, kind='hex')
plt.savefig("sns-jointplot.png")
plt.close()