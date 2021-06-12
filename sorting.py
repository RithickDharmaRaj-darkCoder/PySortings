# Controlling of sort...
from sort_lst import *
aval_sort = ('Bubble Sort','Selection Sort','Insertion Sort','Merge Sort')
print('Available Sortings...')
count = 1
for i in aval_sort:
    print(f'    {count}. {i},')
    count += 1
sort_iput = input("Enter one sorting method name : ").upper()

if (sort_iput == 'BUBBLE SORT' or sort_iput == 'BUBBLE'):
    bubblesort()
elif (sort_iput == 'SELECTION SORT' or sort_iput == 'SELECTION'):
    selection()
elif (sort_iput == 'INSERTION SORT' or sort_iput == 'INSERTION'):
    insertion()
elif (sort_iput == 'MERGE SORT' or sort_iput == 'MERGE'):
    merge()
else:
    print("Invalid Answer!")