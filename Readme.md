# QuickSorts
---
This project generates a csv file with a given amount of random numbers. This csv file is then sorted through either a left most quicksort, median of three quicksort, or an optimised version which picks between Insertion Sort and Quick Sort according to the array size.

### Params
---
- Algorithm name :: (QuickSort/ SortMedianOfThree/ OptimsedSort)
- Size of array to be sorted :: (If you have a csv file already, write 0)
- Unique list :: 0 = duplicate values, 1 = unique values
- Shuffle :: 0 = not shuffled, 1 = slightly shuffled, 2 = shuffled thoroughly
- Repeat :: The number of time the sorting algorithm will repeat itself. This is used to generate a log log graph of all three algorithms.
- Input file name :: (If you have a csv file already, provide name here. File has to be in dir)
- Output file name

### Updates
---
#### v1.1
Rework of quicksort algorithms. Quicksort algorithms are now implemented through [trampolining](https://en.wikipedia.org/wiki/Trampoline_(computing)). This means that the sorting algorithms can now support larger arrays without raising a stack overflow error (due to deep recursion). Tested for up to arrays of 312500 numbers.
![alt text](http://image.prntscr.com/image/b4ebd11f22334e3193cdbbd0041a80f3.png "Log Log Graphs")
---
#### v1.0
More parameters added. Support for 3 different shuffles and duplicates in list. 
Fix for save path for input and output files.