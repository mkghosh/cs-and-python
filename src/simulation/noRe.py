'''
Lecture 5 Problem 1
'''

import random

def oneTrial():
    balls = ['r', 'r', 'r', 'b', 'b', 'b']
    chosen = []

    for _ in xrange(3):
        ball = random.choice(balls)
        balls.remove(ball)
        chosen.append(ball)

    if chosen[0] == chosen[1] and chosen[1] == chosen[2]:
        return True
    return False


def noReplacementSimulation(numTrials):
    numTrue = 0
    for _ in xrange(numTrials):
        if oneTrial():
            numTrue += 1

    return float(numTrue) / float(numTrials)


if __name__  == '__main__':
    print noReplacementSimulation(5000)
