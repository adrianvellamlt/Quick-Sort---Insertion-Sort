import time
import numpy as np
import hashlib
import quicksort as qsort
import sys
qs = qsort.QuickSort()

definitions = {
    'CSVFileName' : 'randomNumDump.csv',
    'Output': 'output.csv'
}

def TimedSortFunction(funcname, *args):
    startTime = time.time()
    func = ChooseAlgorithm(funcname)
    arr = func(*args)

    np.savetxt(definitions['Output'], arr, fmt='%d', delimiter=',')
    print(hashlib.sha512(', '.join([str(x) for x in arr]).encode('utf-8')).hexdigest())

    elapsedTime = time.time() - startTime
    print('function [{}] finished in {} ms'.format(
        func.__name__, int(elapsedTime * 1000)))

def NewArrayToCSV(size, isUnique = True):
    arr = []
    if not isUnique:
        arr = list(np.random.choice(size//4, size, replace=True))
    if isUnique:
        arr = list(np.random.choice(size, size, replace=False))
        set(arr)
    print('Array Size ::', len(arr))
    np.savetxt(definitions['CSVFileName'], arr, fmt='%d', delimiter=',')

def CSVToArray():
    return list(np.genfromtxt(definitions['CSVFileName'], delimiter=',', dtype=None))

def ChooseAlgorithm(func):
    return {
        qs.QuickSort.__name__: qs.QuickSort,
        qs.SortMedianOfThree.__name__: qs.SortMedianOfThree,
        qs.OptimisedSort.__name__: qs.OptimisedSort
    }.get(func, qs.QuickSort)

def InitialSetup():
    chosenAlgorithm = ''
    arrSize = 0

    if len(sys.argv) > 1:
        chosenAlgorithm = sys.argv[1]
        arrSize = sys.argv[2]
        definitions['CSVFileName'] = sys.argv[3]
        definitions['Output'] = sys.argv[4]
    else:
        chosenAlgorithm = input('Write the algorithm to be used: (QuickSort, SortMedianOfThree, OptimisedSort):\n')
        arrSize = input('Write the size of the array:\n')
        definitions['CSVFileName'] = input('Write input file name:\n')
        definitions['Output'] = input('Write output file name:\n')

    if not definitions['CSVFileName'].endswith('.csv'):
        definitions['CSVFileName'] = definitions['CSVFileName'] + '.csv'
    if not definitions['Output'].endswith('.csv'):
        definitions['Output'] = definitions['Output'] + '.csv'

    NewArrayToCSV(int(arrSize))
    return chosenAlgorithm