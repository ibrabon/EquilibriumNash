import argparse


def fromFileToMap(filePath):
    newDict = {}
    with open(filePath) as f:
        for line in f:
            splitLine = line.split()
            newDict[splitLine[0]] = ",".join(splitLine[1:])
    return newDict


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filePath', default="files/income.txt")
    parser.add_argument('-i', '--iterations', default=1)
    return parser.parse_args()


def lcm(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)


def add(x, y):
    return list(map(lambda a, b: a + b, x, y))
