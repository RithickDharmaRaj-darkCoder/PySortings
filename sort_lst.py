# Collection of sorting methods..=

def bubblesort():
    print('----------  BUBBLE SORT ----------')
    lst = []
    lsize = int(input("Enter how many elements to be insert : "))
    for i in range(lsize):
        elst = int(input(f"Add Element {i+1} : "))
        lst.append(elst)
    print("Before Bubble Sort : ", lst)
    for i in range(len(lst) - 1):
        for outer in range(len(lst) - 1):
            if lst[outer] > lst[outer + 1]:
                lst[outer], lst[outer + 1] = lst[outer + 1], lst[outer]
    print("After Bubble Sort  : ", lst)

def selection():
    print('----------  SELECTION SORT ----------')
    lst = []
    lsize = int(input("Enter how many elements to be insert : "))
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
    print("After Selection Sort  : ", lst)

def insertion():
    print('----------  INSERTION SORT ----------')
    lst = []
    lsize = int(input("Enter how many elements to be insert : "))
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
    print(f'After Insertion Sort  : {lst}')

def merge():
    print('----------  MERGE SORT ----------')
    lsize = int(input('How many numbers want to insert : '))
    lst = [int(input(f'Add Number {i + 1} : ')) for i in range(lsize)]
    print(f'Before Merge Sort : {lst}')

    def merging2list(lft, right):
        result = []
        i, j = 0, 0
        while i < len(lft) and j < len(right):
            if lft[i] < right[j]:
                result.append(lft[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += lft[i:]
        result += right[j:]
        return result

    def divide(lst):
        if len(lst) <= 1:
            return lst
        else:
            mid_val = len(lst) // 2
            lft = divide(lst[:mid_val])
            right = divide(lst[mid_val:])
            return merging2list(lft, right)

    print(f'After Merge Sort  : {divide(lst)}')

def heap():
    print('----------  HEAP SORT ----------')
    lsize = int(input('How many numbers want to insert : '))
    lst = [int(input(f'Add Number {i + 1} : ')) for i in range(lsize)]
    print(f'Before Heap Sort : {lst}')
    n = len(lst)

    def heapify(lst, n, p_index):
        largest = p_index
        left_child_index = p_index * 2 + 1
        right_child_index = p_index * 2 + 2

        if left_child_index < n and lst[largest] < lst[left_child_index]:
            largest = left_child_index
        if right_child_index < n and lst[largest] < lst[right_child_index]:
            largest = right_child_index
        if largest != p_index:
            lst[p_index], lst[largest] = lst[largest], lst[p_index]
            heapify(lst, n, largest)

    def heapsort(lst):
        for p_index in range(n // 2 - 1, -1, -1):
            heapify(lst, n, p_index)
        for len in range(n - 1, 0, -1):
            lst[len], lst[0] = lst[0], lst[len]
            heapify(lst, len, 0)
        return lst

    print(f'After Heap Sort  : {heapsort(lst)}')

def quick():
    print('----------  QUICK SORT ----------')
    lsize = int(input('How many numbers want to insert : '))
    lst = [int(input(f'Add Number {i + 1} : ')) for i in range(lsize)]
    print(f'Before Quick Sort : {lst}')

    def quicksort(lst):
        n = len(lst)
        if n <= 1:
            return lst
        else:
            key = lst.pop()

        lower_elements = []
        greater_elements = []

        for element in lst:
            if element < key:
                lower_elements.append(element)
            else:
                greater_elements.append(element)

        return quicksort(lower_elements) + [key] + quicksort(greater_elements)

    print(f'After Quick Sort  : {quicksort(lst)}')