import numpy as np
import random as rand
def squared(x):
    return x**2


def array(size):
    return np.array([[0]*size]*size)

def lattice(size):
    lattice = array(size)
    decider = [0,1]
    for i in (size):
        for j in (size):
            if rand.choice([0,1]) == 0:
                lattice[i][j] = -1
                else:
                    lattice[i][j] = 1
    return lattice
print(lattice(5))






