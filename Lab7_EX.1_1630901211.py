def bubblesort(arraylist):
    trade = False
    for n in range(len(arraylist)-1, 0, -1):
        for i in range(n):
            if arraylist[i] > arraylist[i + 1]:
                swapped = True
                arraylist[i], arraylist[i + 1] = arraylist[i + 1], arraylist[i]
        if not trade:
            return
arraylist = [20,10, 30, 50,70,60, 80,90,100,]
print("Unsorted array list :,")
print(arraylist)
bubblesort(arraylist)
print("Sorted array list :, ")
print(arraylist)