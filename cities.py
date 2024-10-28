import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

cities = pd.read_csv('california_cities.csv')
print(cities.info())

lat = cities['latd']
lon = cities['longd']
pop = cities['population_total']
area = cities['area_land_sq_mi']

plt.scatter(lon, lat, label=None, c=np.log10(pop), cmap='viridis', s=area,linewidth=0, alpha=0.5)

plt.axis('equal')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.colorbar(label='log$_(10)$(population)')
plt.clim(3,7)
plt.title('CA Citieis: Area and Population')

for area in [100, 300,500]:
    plt.scatter([],[], c='k', alpha=0.3, s=area, label=str(area) +'KM$^2$')
plt.legend(scatterpoints=1, frameon=False, labelspacing=1)
plt.savefig('california.png')