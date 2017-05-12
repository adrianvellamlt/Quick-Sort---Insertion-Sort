#<editor-fold desc="Imports">
import quicksort as qsort
import utils as u
#</editor-fold>

#<editor-fold desc="Initialisation">
qs = qsort.QuickSort()
#</editor-fold>

def main():
    u.TimedSortFunction(u.InitialSetup())

if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
        print(ex)