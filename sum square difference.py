def makeList(start,stop):
	list = []
	for iteration in range(start,stop + 1):
		list.append(iteration)
		
	return list


def sumSquareDif(start,stop):
	list = makeList(start,stop)
	sqFun = lambda x: x ** 2
	newList = []
	
	for iteration in list:
		newList.append((sqFun(iteration)))
	
	count = 0
	
	while count < len(newList):
		print(newList[count])
		count += 1
sumSquareDif(1,10)
