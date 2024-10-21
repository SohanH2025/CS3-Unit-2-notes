import matplotlib.pyplot as plt
import numpy as np


plt.style.use('seaborn-v0_8-dark')
print(plt.style.available)

#x is indepentent variable 
x_vals = np.linspace(0,10,100)

#line plots are good when graphing functions
plt.plot(x_vals, np.sin(x_vals))
plt.plot(x_vals, np.cos(x_vals))

#plt.show()

plt.savefig('lineplot.png')

#alt use figure
fig = plt.figure()
ax = plt.axes()

ax.plot(x_vals, np.tan(x_vals), color='red')

fig.savefig('lineplot2.png')