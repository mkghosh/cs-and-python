#!/usr/bin/env python3

def alphaSub(string):
    """
    Function returns the longest substring of input string
    in which the letters occur in alphabetical order.
    """
    start = 0
    end = len(string) - 1
    index = 0
    res = []
    while index < end:
        if string[index] <= string[index+1]:
            partition = string[start : index+2]
            res.append(partition)
        if string[index] > string[index+1]:
            start = index + 1
        index += 1
    if res == []:
        res.append(string[0])

    tmp = res[0]
    for i in range(len(res)-1):
        if len(tmp) < len(res[i+1]):
            tmp = res[i+1]
    return tmp


if __name__ == '__main__':
    s1 = "azcbobobegghakl"
    s2 = "zyxwvutsrqponmlkjihgfedcba"
    s3 = "fhgafpqtgoboupdt"
    s4 = "hfdwstbndftxxqp"
    s5 = "fwtnplhvgqqnqizzsx"
    print(alphaSub(s1))
    print(alphaSub(s2))
    print(alphaSub(s3))
    print(alphaSub(s4))
    print(alphaSub(s5))
