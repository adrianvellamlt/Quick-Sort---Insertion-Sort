import insertionsort as ins

class QuickSort(object):
    def QuickSort(self, arr):
        if len(arr) <= 1:
            return arr
        return QuickSort.QuickSort(self, [x for x in arr[1:] if x < arr[0]]) + [arr[0]] + QuickSort.QuickSort(self, [x for x in arr[1:] if x >= arr[0]])

    def SortMedianOfThree(self, arr):
        QuickSort.QuickSortWithMedian(self, arr, 0, len(arr))
        return arr

    def OptimisedSort(self, arr):
        if len(arr) > 16:
            return QuickSort.SortMedianOfThree(self, arr)
        return ins.InsertionSort().Sort(arr)

    def QuickSortWithMedian(self, array, leftindex, rightindex):
        if leftindex < rightindex:
            newpivotindex = QuickSort.Partition(self, array, leftindex, rightindex)
            QuickSort.QuickSortWithMedian(self, array, leftindex, newpivotindex)
            QuickSort.QuickSortWithMedian(self, array, newpivotindex + 1, rightindex)

    def Partition(self, array, leftend, rightend):
        def Swap(j):
            nonlocal i
            array[j], array[i] = array[i], array[j]
            i += 1
        def Switch(index):
            return {
                0: leftend,
                1: middleIndex,
                2: rightend - 1
            }[index]    # Makeshift switch statement
        def GetMiddleIndex(leftend, length):
            if length % 2 == 0: return leftend + length // 2 - 1
            else: return leftend + length // 2

        left = array[leftend]
        right = array[rightend - 1]
        length = rightend - leftend
        middleIndex = GetMiddleIndex(leftend, length)
        middle = array[middleIndex]

        pivot = QuickSort.Median(self, left, right, middle)
        tmpArr = [left, middle, right]
        pivotindex = Switch(tmpArr.index(pivot))

        array[pivotindex], array[leftend] = array[leftend], pivot
        i = leftend + 1
        [Swap(j) for j in range(leftend + 1, rightend) if array[j] < pivot]
        array[leftend], array[i - 1] = array[i - 1], array[leftend]
        return i - 1    # New Pivot

    def Median(self, i, j, k):
        if i < j:
            return j if j < k else k
        else:
            return i if i < k else k