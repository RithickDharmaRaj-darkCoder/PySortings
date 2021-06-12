# Collection of sorting methods..=

def bubblesort():
    lst = []
    lsize = int(input("\nEnter how many elements to be insert : "))
    for i in range(lsize):
        elst = int(input(f"Add Element {i+1} : "))
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
        elst = int(input(f"Add Element {i+1} : "))
        lst.append(elst)
    print("Before Selection Sort : ", lst)

    for outer in range(len(lst) - 1):
        min_index = outer
        for inner in range(outer + 1, len(lst)):
            if lst[min_index] > lst[inner]:
                min_index = inner
        if lst[outer] != lst[min_index]:
            lst[outer], lst[min_index] = lst[min_index], lst[outer]
    print("After Selection Sort : ", lst)

def insertion():
    lst = []
    lsize = int(input("\nEnter how many elements to be insert : "))
    for i in range(lsize):
        elst = int(input(f"Add Element {i + 1} : "))
        lst.append(elst)
    print(f'Before Insertion Sort : {lst}')

    for index in range(1, len(lst)):
        curent_value = lst[index]
        postion = index
        while (curent_value < lst[postion - 1]) and (postion > 0):
            lst[postion] = lst[postion - 1]
            postion -= 1
        lst[postion] = curent_value
    print(f'After Insertion Sort : {lst}')

def merge():
    def mergesort(lst):
        if len(lst) > 1:
            mid = len(lst) // 2
            lft_lst = lst[:mid]
            right_lst = lst[mid:]
            mergesort(lft_lst)
            mergesort(right_lst)

            (i, j, k) = (0, 0, 0)
            while len(lft_lst) > i and len(right_lst) > j:
                if lft_lst[i] < right_lst[j]:
                    lst[k] = lft_lst[i]
                    i += 1
                    k += 1
                else:
                    lst[k] = right_lst[j]
                    j += 1
                    k += 1

            while len(lft_lst) > i:
                lst[k] = lft_lst[i]
                i += 1
                k += 1
            while len(right_lst) > j:
                lst[k] = right_lst[j]
                j += 1
                k += 1

    lsize = int(input('How many numbers want to add : '))
    lst = [int(input(f'Add number {i + 1} : ')) for i in range(lsize)]
    print(f'Before Merge Sort : {lst}')
    mergesort(lst)
    print(f'After Merge Sort : {lst}')