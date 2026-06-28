from latticechange import sweeps
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.colors import ListedColormap, BoundaryNorm

from latticechange import sweeps
basis = sweeps(50, 0.00, 0.95,30)
xvalues = basis[2]
yvalues = basis[1]
finallattice = basis[0]

cmap = ListedColormap(['black','white'])
bounds = [-1.5,0,1.5]
norm = BoundaryNorm(bounds, cmap.N)


plt.figure(1)
plt.xlabel('Number of sweeps')
plt.ylabel(' Magnetisation of lattice')
plt.plot(xvalues,yvalues)
plt.show()
plt.savefig('mag graph.png')

plt.figure(2)
plt.imshow(finallattice, cmap = cmap, norm = norm )
plt.colorbar(ticks = [-1,1])
plt.savefig('final lattice.png')
print(finallattice)
