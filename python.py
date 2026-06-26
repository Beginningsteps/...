import numpy as np
import random as rand
def main():
    lattice(5)


def array(size):
    return np.array([[0]*size]*size)

def lattice(size):
    lattice = array(size)
    decider = [0,1]
    for i in range(size):
        for j in range(size):
            if rand.choice([0,1]) == 0:
                lattice[i][j] = -1
            else:
                lattice[i][j] = 1
    return lattice



if __name__ == '__main__':
    main()







