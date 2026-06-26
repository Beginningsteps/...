import numpy as np
from python import lattice
import random as rand

def main():
    sweeps(5,1,2,3)

def sweeps(size, B,J,n):
    givenlattice = lattice(size)
    f = 0
    deltaE = 0
    r = 0
    MagnetisationList = []
    Mag = 0
    sweepslist = []
    for sweep in range(n):
        sweepslist = sweepslist + [sweep]

        for i in range(size):
            for j in range(size):
                r = rand.random()
                f = givenlattice[i-1][j] + givenlattice[i - size +1][j] + givenlattice[i][j - 1] + givenlattice[i][j - size +1]
                deltaE =-2*(J*f +B)*givenlattice[i][j]
                if np.e**(-deltaE) > 1:
                     givenlattice[i][j] = -givenlattice[i][j]
                elif np.e**(-deltaE) > r:
                     givenlattice[i][j] = -givenlattice[i][j]
                else:
                    givenlattice[i][j] = givenlattice[i][j]
        Mag = np.mean(givenlattice)
        MagnetisationList = MagnetisationList + [Mag]
        
        
    return givenlattice
    return MagnetisationList
    return sweepslist

if __name__ == '__main__':
    main()

