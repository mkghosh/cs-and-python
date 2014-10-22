'''
L13 lecture problems
'''

import random

# P2
def genEven():
    '''
    returns a random even number  x, where 0 <= x < 100
    '''
    return random.randrange(0, 100, 2)


# P3a
def deterministicNumber():
    '''
    deterministically generates and returns an even number between 9 and 21
    '''
    random.seed(0)
    return random.randint(5, 10) * 2


# P3b
def stochasticNumber():
    '''
    stochastically generates and returns
    a uniformly distributed even number between 9 and 21
    '''
    # return random.randint(5, 10) * 2
    return random.randrange(10, 22, 2)


# P4
# their are some equivalent uniform distributions.

def dist1():
    return random.random() * 2 - 1

def dist2():
    if random.random() > 0.5:
        return random.random()
    else:
        return random.random() - 1

# both dist1 and dist2 are a uniform distribution over [-1.0, 1.0).

def dist3():
    return int(random.random() * 10)

def dist4():
    return random.randrange(0, 10)

# the random.random() distribution is uniform,
# and so is the random.randrange() distribution,
# so both dist3 and dist4 are a discrete uniform distribution over [0, 9].
