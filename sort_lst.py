# Collection of sorting methods..=

def bubblesort():
    lst = []
    lsize = int(input("\nEnter how many elements to be insert : "))
    for i in range(lsize):
        elst = int(input("Enter the elements to add it in list : "))
        lst.append(elst)
    print(lst)

    for outer in range(len(lst)-1,0,-1):
        for inner in range(outer):
            if lst[inner] > lst[outer]:
                temp = lst[inner]
                lst[inner] = lst[outer]
                lst[outer] = temp
    print(lst)