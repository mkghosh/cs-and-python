'''
module of 6.00.2x lecture 4 lecture-in question 3
'''

def stdDev(seq):
    length = float(len(seq))
    mean = sum(seq) / length 
    total = 0.0
    for ele in seq:
        total += (ele - mean)**2

    return (total / length)**0.5


def stdDevOfLengths(seq):
    '''
    seq: a list of strings

    returns the standard deviation of the lengths of the strings,
    or NaN if seq is empty
    '''
    length = float(len(seq))

    if length == 0.0:
        return float('NaN')

    # compute mean
    mean = sum([len(string) for string in seq]) / length

    # compute variance (average squared deviation from mean)
    sumDev = 0
    for string in seq:
        sumDev += (len(string) - mean)**2
    variance = sumDev / length

    # standard deviation is the square root of the variance
    return variance**0.5


def cVariation(seq):
    mean = sum(seq) / float(len(seq))
    try:
        return stdDev(seq) / mean
    except ZeroDivisionError:
        return float('NaN')


if __name__ == '__main__':
    print(cVariation([10, 4, 12, 15, 20, 5]))
