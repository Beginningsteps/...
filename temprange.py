import numpy as np
from lattice import lattice
import random as rand


def main():
    temprange(1,1,1,1,1,2000)

def temprange(size, B, J, n, largeT1, largeT2):
    Tlist = []
    MagTList = []
    
    refTList = []
    data = lattice(size)
    for i in range(largeT1, largeT2 + 1):
        Tlist = Tlist + [i/1000]
        for sweepnum in range(n):

            for j in range(size):
                for k in range(size):
                    r = rand.random()
                    f = data[j-1][k] + data[j - size +1][k] + data[j][k - 1] + data[j][k - size +1]
                    if B == 0:
                        deltaE =2*(J*f)*data[j][k]/(i/1000)
                    else:
                        deltaE =2*(J*f +B)*data[j][k]/(i/1000)

                    if np.e**(-deltaE) > 1:
                         data[j][k] = -data[j][k]
                    elif np.e**(-deltaE) > r:
                         data[j][k] = -data[j][k]
                    else:
                        data[j][k] = data[j][k]
        MagTList = MagTList + [abs(np.mean(data))]
        if type(1-(i/2.269)**0.125) == np.float64 or np.int64:
            refTList = refTList + [(1-i/2.269)**0.125]
        else:
            refTList = refTList + [0]

    return Tlist, MagTList, refTList

if __name__ == '__main__':
    main()