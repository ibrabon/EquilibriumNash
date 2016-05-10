import argparse

class Util:

    @staticmethod
    def fromFileToMap(filePath):
        newDict = {}
        with open(filePath) as f:
            for line in f:
                splitLine = line.split()
                newDict[splitLine[0]] = ",".join(splitLine[1:])
        return newDict

    @staticmethod
    def parse():
        parser = argparse.ArgumentParser()
        parser.add_argument('-f', '--filePath', default="files/income.txt")
        parser.add_argument('-i', '--iterations')
        return parser.parse_args()
