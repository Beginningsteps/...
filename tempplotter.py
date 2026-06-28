from temprange import temprange
import numpy as np
import matplotlib.pyplot as plt

Tbasis = temprange(50, 0, 0.95, 300, 2700)
xvalues = Tbasis[0]
yvalues = Tbasis[1]

plt.figure(1)

plt.scatter(xvalues, yvalues)
plt.xlabel('Temperature Values')
plt.ylabel('Magnetisation')
plt.savefig('2nd order transition')