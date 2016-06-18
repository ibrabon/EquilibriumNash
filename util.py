import argparse
import os
import re

import matplotlib.pyplot as plt
import scipy.stats.stats as st
from numpy import std


def fromFileToMap(filePath):
    newDict = {}
    with open(filePath) as f:
        for line in f:
            line = re.split("#", line)
            splitLine = line[0].split()
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


def make_histogramm(array, player_name, path):
    plt.hist(array, histtype='step')
    file_name = str(player_name) + ".png"
    try:
        os.mkdir(path, mode=0o777)
    except OSError:
        pass
    plt.savefig(path + file_name, format='png')


def make_all_calculations(array, player_name, file):
    file.write(str(player_name + "'s average = " + str(float(sum(array)) / len(array)) + "\n"))
    file.write(str(player_name + "'s standard deviation = " + str(std(array)) + "\n"))
    file.write(str(player_name + "'s asymmetry = " + str(st.skew(array, bias=False)) + "\n"))
    file.write(str(player_name + "'s excess = " + str(st.kurtosis(array, bias=False)) + "\n"))


def create_all_stats(array, player_name, time):
    path = "results/game" + str(time) + "/"
    make_histogramm(array, player_name, path)

    file = open(path + "allEquations.txt", "a")
    make_all_calculations(array, player_name, file)
