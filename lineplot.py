import matplotlib.pyplot as plt
import numpy as np


plt.style.use('seaborn-v0_8-dark')
print(plt.style.available)

#x is indepentent variable 
x_vals = np.linspace(0,10,1000)

#line plots are good when graphing functions
plt.plot(x_vals, np.sin(x_vals))
plt.plot(x_vals, np.cos(x_vals))

#plt.show()

plt.savefig('lineplot.png')

#alt use figure
fig = plt.figure()
ax = plt.axes()

ax.plot(x_vals, np.tan(x_vals), color='red')
ax.plot(x_vals, x_vals, color='green', linestyle='dashed')
ax.plot(x_vals, 2*x_vals, color='yellow', linestyle='dashed')

ax.plot(x_vals, -x_vals*x_vals, '--c')

fig.savefig('lineplot2.png')

fig3 = plt.figure()
ax3 = plt.axes()

plt.plot(x_vals, np.sin(x_vals), label ="sin(x)")
plt.xlim(-1,11)
plt.ylim(-10,10)

#plt.axis('tight')

#add titles /labels
plt.title('a sin wave')
plt.xlabel("x")
plt.ylabel("sin(x)")
#add legend 
plt.legend()

fig3.savefig('lineplot3.png')
