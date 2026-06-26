from latticechange import sweeps
import numpy as np 
import matplotlib.pyplot as plt 

from latticechange import sweeps
basis = sweeps(50, -0.05, 0.95,30)
xvalues = basis[2]
yvalues = basis[1]


plt.figure()
plt.xlabel('Number of sweeps')
plt.ylabel(' Magnetisation of lattice')
plt.plot(xvalues,yvalues)


plt.show()
plt.savefig('mag graph.png')