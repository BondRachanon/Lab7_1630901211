def insertionsort(arraylist):
	for i in range(1, len(arraylist)):
		key = arraylist[i]
		j = i-1
		while j >=0 and key < arraylist[j] :
				arraylist[j+1] = arraylist[j]
				j -= 1
		arraylist[j+1] = key
arraylist = [20, 40, 50, 10, 30]
print("Insertion arraylist :",arraylist)
print("=======================")
insertionsort(arraylist)
print("Insertionsort arraylist : ")
print(arraylist)