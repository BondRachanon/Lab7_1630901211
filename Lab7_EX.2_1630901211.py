def selectionSort(Arr, S):
    for ind in range(S):
        minind = ind
        for j in range(ind + 1, S):
            if Arr[j] < Arr[minind]:
                minind = j
        (Arr[ind], Arr[minind]) = (Arr[minind], Arr[ind])
arraylist = [80, 30, 10, 70, 60, 20, 40, 50]
size = len(arraylist)
print("Arraylist is:",arraylist)
print("==============================================")
selectionSort(arraylist, size)
print('Array list selection sort is:')
print(arraylist)
