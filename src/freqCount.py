#!/usr/bin/env python3

def freqCount(keywords, string):
    """
    Function count the number of times multiple keywords occur in a string.

    Input: 1D sequence(keywords), str(string)
    Output: dict(keyword= times)
    """
    res = {keyword: 0 for keyword in keywords}
    for partition in res.keys():
        for index in range(len(string)):
            if string[index : index+len(partition)] == partition:
                res[partition] += 1
    return res


if __name__ == '__main__':
    string = 'azcbobobeggeegghakakakakakil'
    keywords = ['bob', 'egg', 'aka']

    res = freqCount(keywords, string)
    print(res)

