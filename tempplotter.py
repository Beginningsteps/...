from temprange import temprange
import numpy as np
import matplotlib.pyplot as plt

Tbasis = temprange(50, 0, 0.95, 300,1, 3700)
xvalues = Tbasis[0]
yvalues = Tbasis[1]
y2values = Tbasis[2]
y3values = np.array(yvalues)-np.array(y2values)

plt.figure(1)

plt.plot(xvalues, yvalues, label = 'Experimental')
plt.plot(xvalues, y2values, label = 'Theory')
plt.plot(xvalues, y3values, label = 'Residuals')
plt.xlabel('Temperature Values')
plt.ylabel('Magnetisation')

plt.legend()
plt.savefig('2nd order transition and residues')
