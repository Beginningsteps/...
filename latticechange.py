import numpy as np
from python import lattice
import random as rand

def sweeps(size, B,J,n):
    givenlattice = lattice(size)
    f = 0
    deltaE = 0
    r = 0
    Magnetisation = []
    for sweeps in range(n):
        for i in range(size):
            for j in range(size):
                r = rand.choice()
                f = givenlattice[i + size -1][j] + givenlattice[i+1][j] + givenlattice[i][j + size -1] + givenlattice[i][j+1]
                deltaE =-2*(J*f +B)*givenlattice[i][j]
                if np.e**(-deltaE) > 1:
                     givenlattice[i][j] = -givenlattice[i][j]
                elif np.e**(-deltaE) > r:
                     givenlattice[i][j] = -givenlattice[i][j]
                else:
                    givenlattice[i][j] = givenlattice[i][j]
    return givenlattice

