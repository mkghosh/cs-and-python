# Given a linear function with a positive slope that 
# intercepts the x axis between 0 and 100, find the 
# point where it intercepts without solving for x. 
# Use bisection search. 
# In other words, find 'a' such that f(a) = 0 to some certainty 'epsilon'.

def f(x):
    return -5+2.77*x

def g(x):
    return -5+0.08*x

def h(x):
    return -50+x
    
# function that computes x interecpt using bisection
def intercept_bisection(func, epsilon):
    ''' func is a function
        epsilon is some small float
    '''
    low = 0
    high = 100
    mid = (high + low)/2.0
    
    # remember to take absolute value of f(x)
    while (abs(func(mid)) > epsilon):
        # case where guess was too low
        if func(mid) > 0:
            high = mid
        # case where guess was too high
        elif func(mid) < 0:
            low = mid
        # recalculate guess with new high and low values
        mid = (high + low)/2.0
    return mid
    
print intercept_bisection(g, 0.1)
