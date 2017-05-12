#<editor-fold desc="Imports">
import insertionsort as ins
#</editor-fold>

class QuickSort(object):
    def GetMedianOfThreeIndex(self, array, start, end):
        def Switch(index):
            nonlocal medianIndex
            return {
                0: start,
                1: medianIndex,
                2: end - 1
            }[index]  # Makeshift switch statement

        def GetMedianIndex(start, length):
            if length % 2 == 0:
                return start + length // 2 - 1
            else:
                return start + length // 2

        def Median(i, j, k):
            if i < j:
                return j if j < k else k
            else:
                return i if i < k else k

        medianIndex = GetMedianIndex(start, end - start)
        return Median(array[start], array[end - 1], array[medianIndex])

    def Partition(self, array, start, end, isMedianOfThree):
        medianIndex = QuickSort.GetMedianOfThreeIndex(self, array, start, end) if isMedianOfThree else start
        pivot = array[medianIndex]

        array[medianIndex], array[start] = array[start], pivot
        i = start + 1
        for j in range(start + 1, end):
            if array[j] < pivot:
                array[j], array[i] = array[i], array[j]
                i += 1
        array[start], array[i - 1] = array[i - 1], array[start]
        return i - 1  # New Pivot

    def Sort(self, arr, isMedianOfThree):
        stack = []
        stack.append(0)
        stack.append(len(arr))
        while len(stack) > 0:
            end = stack.pop()
            start = stack.pop()
            if end - start < 2: continue
            p = QuickSort.Partition(self, arr, start, end, isMedianOfThree)

            stack.append(p + 1)
            stack.append(end)

            stack.append(start)
            stack.append(p)

    def QuickSort(self, arr):
        if len(arr) <= 1:
            return arr
        QuickSort.Sort(self, arr, False)
        return arr

    def SortMedianOfThree(self, arr):
        if len(arr) <= 1:
            return arr
        QuickSort.Sort(self, arr, True)
        return arr

    def OptimisedSort(self, arr):
        if len(arr) > 16:
            return QuickSort.SortMedianOfThree(self, arr)
        return ins.InsertionSort().Sort(arr)