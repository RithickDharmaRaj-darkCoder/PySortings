# Controlling of sort...
from sort_lst import *
aval_sort = ['Bubble']
print("Availabe Sorting Methods : ",aval_sort)
sort_iput = input("Enter one sorting method name : ").upper()

if sort_iput == 'BUBBLE':
    bubblesort()
elif sort_iput == 'SELECTION':
    selection()
else:
    print("Invalid Answer!")