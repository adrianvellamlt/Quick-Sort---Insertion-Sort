#<editor-fold desc="Imports">
import time
import numpy as np
import hashlib
import quicksort as qsort
import sys, os
from random import randint
#</editor-fold>

#<editor-fold desc="Initialisation">
qs = qsort.QuickSort()
timeArray = []
arr = []
chosenAlgorithm = ''
arrSize = 0
isUnique = 1
shuffle = 0
repeat = 0
#</editor-fold>

definitions = {
    'CSVFileName' : 'randomNumDump.csv',
    'Output': 'output.csv',
    'TimeLog': 'timelog.csv'
}

def TimedSortFunction(function):
    global timeArray
    global arr
    global repeat

    for i in range(int(repeat)):
        arr = SetupUpArray()

        startTime = time.time()
        func = ChooseAlgorithm(function)
        arr = func(arr)
        elapsedTime = time.time() - startTime

        print(hashlib.sha512(', '.join([str(x) for x in arr]).encode('utf-8')).hexdigest())

        print('{}. function [{}] finished in {} ms'.format(i,
            func.__name__, elapsedTime*1000))
        timeArray.append(elapsedTime*1000)

    timeArray.append('Mean :: {0}'.format(sum(timeArray)/len(timeArray)))
    np.savetxt(definitions['TimeLog'], timeArray, fmt='%s', delimiter=',')
    np.savetxt(definitions['Output'], arr, fmt='%d', delimiter=',')

def NewArrayToCSV(size, isUnique, shuffle):
    arr = list(np.random.choice(size, size, replace=not isUnique))
    print('Array Size ::', len(arr))
    if shuffle is '0':
        arr.sort()
    elif shuffle is '1':
        arr.sort()
        arr = SlightlyShuffle(arr)
    np.savetxt(definitions['CSVFileName'], arr, fmt='%d', delimiter=',')

def CSVToArray(path):
    return list(np.genfromtxt(path, delimiter=',', dtype=None))

def ChooseAlgorithm(func):
    return {
        qs.QuickSort.__name__: qs.QuickSort,
        qs.SortMedianOfThree.__name__: qs.SortMedianOfThree,
        qs.OptimisedSort.__name__: qs.OptimisedSort
    }.get(func, qs.QuickSort)

def InitialSetup():
    global chosenAlgorithm
    global arrSize
    global isUnique
    global shuffle
    global repeat

    if len(sys.argv) > 1:
        chosenAlgorithm = sys.argv[1]
        arrSize = sys.argv[2]
        isUnique = sys.argv[3]
        shuffle = sys.argv[4]
        repeat = sys.argv[5]
        definitions['CSVFileName'] = sys.argv[6]
        definitions['Output'] = sys.argv[7]
    else:
        chosenAlgorithm = input('Write the algorithm to be used: (QuickSort, SortMedianOfThree, OptimisedSort):\n')
        arrSize = input('Write the size of the array:\n')
        isUnique = input('All unique elements? (0/1)\n')
        shuffle = input('How shuffled should the list be? (0/1/2)\n')
        repeat = input('Repeat sort how many times?\n')
        definitions['CSVFileName'] = input('Write input file name:\n')
        definitions['Output'] = input('Write output file name:\n')

    if not definitions['CSVFileName'].endswith('.csv'):
        definitions['CSVFileName'] = definitions['CSVFileName'] + '.csv'
    if not definitions['Output'].endswith('.csv'):
        definitions['Output'] = definitions['Output'] + '.csv'
    definitions['Output'] = os.path.abspath(os.path.dirname(sys.argv[0])) + '\\' + definitions['Output']

    if (arrSize is not '0'):
        definitions['CSVFileName'] = os.path.abspath(os.path.dirname(sys.argv[0])) + '\\' + definitions['CSVFileName']

    return chosenAlgorithm

def SetupUpArray():
    global arrSize
    global isUnique
    global shuffle

    if (arrSize is not '0'):
        NewArrayToCSV(int(arrSize), True if isUnique is '1' else False, shuffle)

    return CSVToArray(definitions['CSVFileName'])

def SlightlyShuffle(arr):
    for i in range(len(arr)//7):
        randNo1 = randint(0, len(arr) - 1)
        randNo2 = randint(0, len(arr) - 1)
        arr[randNo1], arr[randNo2] = arr[randNo2], arr[randNo1]
    return arr