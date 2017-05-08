# QuickSorts

This project generates a csv file with a given amount of random numbers. 
This csv file is then sorted through either a left most quicksort, median 
of three quicksort, or an optimised version which picks between Insertion 
Sort and Quick Sort according to the array size.

### Params

- Algorithm name :: (QuickSort/ SortMedianOfThree/ OptimsedSort)
- Size of array to be sorted :: (If you have a csv file already, write 0)
- Unique list :: 0 = duplicate values, 1 = unique values
- Shuffle :: 0 = not shuffled, 1 = slightly shuffled, 2 = shuffled thoroughly
- Input file name :: (If you have a csv file already, provide name here. File has to be in dir)
- Output file name

### Update

More parameters added. Support for 3 different shuffles and duplicates in list. 
Fix for save path for input and output files.