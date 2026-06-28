import numpy as np
from lattice import lattice
import random as rand


def main():
    temprange(1,1,1,1,2000)

def temprange(size, B, J, n, largeT):
    Tlist = []
    MagTList = []
    data = lattice(size)
    for i in range(1, largeT + 1):
        Tlist = Tlist + [i/1000]
        for j in range(size):
            for k in range(size):
                r = rand.random()
                f = data[j-1][k] + data[j - size +1][k] + data[j][k - 1] + data[j][k - size +1]
                deltaE =2*(J*f +B)*data[j][k]/(i/1000)
                if np.e**(-deltaE) > 1:
                     data[j][k] = -data[j][k]
                elif np.e**(-deltaE) > r:
                     data[j][k] = -data[j][k]
                else:
                    data[j][k] = data[j][k]
        MagTList = MagTList + [np.mean(data)]
    return Tlist, MagTList

if __name__ == '__main__':
    main()