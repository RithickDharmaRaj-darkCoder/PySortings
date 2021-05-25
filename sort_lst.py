# Collection of sorting methods..=

def bubblesort():
    lst = []
    lsize = int(input("\nEnter how many elements to be insert : "))
    for i in range(lsize):
        elst = int(input("Enter the elements to add it in list : "))
        lst.append(elst)
    print("Before Bubble Sort : ", lst)
    for i in range(len(lst) - 1):
        for outer in range(len(lst) - 1):
            if lst[outer] > lst[outer + 1]:
                lst[outer], lst[outer + 1] = lst[outer + 1], lst[outer]
    print("After Bubble Sort : ", lst)

def selection():
    lst = []
    lsize = int(input("\nEnter how many elements to be insert : "))
    for i in range(lsize):
        elst = int(input("Enter the elements to add it in list : "))
        lst.append(elst)
    print("Before Selection Sort : ", lst)

    for outer in range(len(lst) - 1):
        min_index = outer
        for inner in range(outer + 1, len(lst)):
            if lst[inner] < lst[min_index]:
                min_index = inner
        if lst[outer] != lst[min_index]:
            lst[outer], lst[min_index] = lst[min_index], lst[outer]
    print("After Selection Sort : ", lst)