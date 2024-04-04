myList = [1,3,3,3,3,1]
max = myList[0]
indexOfMax = 0
for x in range(1, len(myList)):
	if myList[x] > max:
		max = myList[x]
		indexOfMax = x

print(indexOfMax)