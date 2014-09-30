#!/usr/bin/env python

def myLog(x, b):
    if not isinstance(x, int) or x <= 0:
        raise ValueError('x must be an positive integer')
    if not isinstance(b, int) or b < 2:
        raise ValueError('b must be an positive integer and b >= 2')

    p = 0
    while b**p <= x:
        p += 1
        if b**p > x:
            return p-1
        elif b**p == x:
            return p


def laceStrings(s1, s2):
    res = ""
    length = min(len(s1), len(s2))
    idx = 0

    while idx < length:
        res += s1[idx]
        res += s2[idx]
        idx += 1

    if len(s1) > len(s2):
        res += s1[idx:]
    if len(s2) > len(s1):
        res += s2[idx:]
    return res


def laceStringRecur(s1, s2):
    def helper(s1, s2, out):
        if s1 == '':
            return out+s2
        if s2 == '':
            return out+s1
        else:
            return helper(s1[1:], s2[1:], out+s1[0]+s2[0])
    return helper(s1, s2, '')


def McNuggets(n):
    cm = [6, 9, 20]
    if n == 0:
        return True
    for i in cm:
        if n >= i and McNuggets(n-i):
            return True
    return False


def fixedPoint(f, epsilon):
    guess = 1.0
    for i in range(100):
        if abs(f(guess) - guess) < epsilon):
            return guess
        else:
            guess = f(guess)
    return guess
