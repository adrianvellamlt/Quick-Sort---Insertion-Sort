class InsertionSort(object):

    def Insert(self, x, arr):
        if not arr: return [x]
        elif x <= arr[0]: return [x] + arr
        else: return [arr[0]] + InsertionSort.Insert(self, x, arr[1:])

    def Sort(self, arr):
        if not arr: return []
        else: return InsertionSort.Insert(self, arr[0], InsertionSort.Sort(self, arr[1:]))