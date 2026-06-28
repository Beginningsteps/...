import numpy as np
from lattice import lattice
import random as rand

def main():
    sweeps(5,1,2,3)

def sweeps(size, B,J,n):
    givenlattice = lattice(size)
    f = 0
    deltaE = 0
    r = 0
    MagnetisationList = [np.mean(givenlattice)]
    sweepslist = [0]
    for sweep in range(1,n+1):
        sweepslist = sweepslist + [sweep]

        for i in range(size):
            for j in range(size):
                r = rand.random()
                f = givenlattice[i-1][j] + givenlattice[i - size +1][j] + givenlattice[i][j - 1] + givenlattice[i][j - size +1]
                deltaE =2*(J*f +B)*givenlattice[i][j]
                if np.e**(-deltaE) > 1:
                     givenlattice[i][j] = -givenlattice[i][j]
                elif np.e**(-deltaE) > r:
                     givenlattice[i][j] = -givenlattice[i][j]
                else:
                    givenlattice[i][j] = givenlattice[i][j]
        Mag = np.mean(givenlattice)
        MagnetisationList = MagnetisationList + [np.mean(givenlattice)]
        
        
    return givenlattice, MagnetisationList , sweepslist

if __name__ == '__main__':
    main()

