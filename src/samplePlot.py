'''
problem 1
'''

import pylab
import numpy


FILE_PATH = '/Users/HexTeto/Documents/Github/cs-and-python/ref/julyTemps.txt'

def loadFiles():
    '''
    function loads temperature data is described as a plain text file
    '''

    high = []
    low = []

    with open(FILE_PATH) as file:
        for line in file:
            fields = line.split()
            if len(fields) != 3 or 'Boston' == fields[0] or 'Day' == fields[0]:
                continue
            else:
                high.append(int(fields[1]))
                low.append(int(fields[2]))

    return (low, high)


def producePlot(lowTemps, highTemps):
    '''
    horizen: days
    vertical: temperature
    '''

    diffTemps = list(numpy.array(highTemps) - numpy.array(lowTemps))

    pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
    pylab.xlabel('Days')
    pylab.ylabel('Temperature Ranges')
    pylab.plot(range(1, 32), diffTemps, color='red', linewidth=2)
    pylab.show()


if __name__ == '__main__':
    (low, high) = loadFiles()
    producePlot(low, high)
