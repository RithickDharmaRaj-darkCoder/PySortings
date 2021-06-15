# Controlling of sort...
from sort_lst import *
aval_sort = ('Bubble Sort','Selection Sort','Insertion Sort','Merge Sort','Heap Sort','Quick Sort')
print('Available Sortings...')
count = 1
for i in aval_sort:
    print(f'    {count}. {i},')
    count += 1
def sortings():
    sort_iput = input("Enter one sorting method name : ").upper()

    if (sort_iput == 'BUBBLE SORT' or sort_iput == 'BUBBLE' or sort_iput == '1'):
        bubblesort()
    elif (sort_iput == 'SELECTION SORT' or sort_iput == 'SELECTION' or sort_iput == '2'):
        selection()
    elif (sort_iput == 'INSERTION SORT' or sort_iput == 'INSERTION' or sort_iput == '3'):
        insertion()
    elif (sort_iput == 'MERGE SORT' or sort_iput == 'MERGE' or sort_iput == '4'):
        merge()
    elif (sort_iput == 'HEAP SORT' or sort_iput == 'HEAP' or sort_iput == '5'):
        heap()
    elif (sort_iput == 'QUICK SORT' or sort_iput == 'QUICK' or sort_iput == '6'):
        quick()
    else:
        print("Invalid Answer!")
        sortings()

sortings()


#Personal Greetings...
print("\nThank You!\n          -darkCoder \U0001F43E")