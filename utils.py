import time
import numpy as np
import hashlib
import quicksort as qsort
import sys, os
from random import randint
qs = qsort.QuickSort()

definitions = {
    'CSVFileName' : 'randomNumDump.csv',
    'Output': 'output.csv'
}

def TimedSortFunction(params):
    startTime = time.time()
    func = ChooseAlgorithm(params[0])
    arr = func(params[1])
    elapsedTime = time.time() - startTime

    np.savetxt(definitions['Output'], arr, fmt='%d', delimiter=',')
    print(hashlib.sha512(', '.join([str(x) for x in arr]).encode('utf-8')).hexdigest())

    print('function [{}] finished in {} ms'.format(
        func.__name__, int(elapsedTime * 1000)))

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
    chosenAlgorithm = ''
    arrSize = 0
    isUnique = 1
    shuffle = 0

    if len(sys.argv) > 1:
        chosenAlgorithm = sys.argv[1]
        arrSize = sys.argv[2]
        isUnique = sys.argv[3]
        shuffle = sys.argv[4]
        definitions['CSVFileName'] = sys.argv[5]
        definitions['Output'] = sys.argv[6]
    else:
        chosenAlgorithm = input('Write the algorithm to be used: (QuickSort, SortMedianOfThree, OptimisedSort):\n')
        arrSize = input('Write the size of the array:\n')
        isUnique = input('All unique elements? (0/1)\n')
        shuffle = input('How shuffled should the list be? (0/1/2)\n')
        definitions['CSVFileName'] = input('Write input file name:\n')
        definitions['Output'] = input('Write output file name:\n')

    if not definitions['CSVFileName'].endswith('.csv'):
        definitions['CSVFileName'] = definitions['CSVFileName'] + '.csv'
    if not definitions['Output'].endswith('.csv'):
        definitions['Output'] = definitions['Output'] + '.csv'
    definitions['CSVFileName'] = os.path.abspath(os.path.dirname(sys.argv[0])) + '/' + definitions['CSVFileName']
    definitions['Output'] = os.path.abspath(os.path.dirname(sys.argv[0])) + '/' + definitions['Output']

    arr = []
    if(arrSize is not 0):
        NewArrayToCSV(int(arrSize),True if isUnique is '1' else False, shuffle)
    arr = CSVToArray(definitions['CSVFileName'])

    return chosenAlgorithm, arr

def SlightlyShuffle(arr):
    for i in range(len(arr)//15):
        randNo1 = randint(0, len(arr))
        randNo2 = randint(0, len(arr))
        arr[randNo1], arr[randNo2] = arr[randNo2], arr[randNo1]
    return arr