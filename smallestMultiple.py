def smallestMultiple(start, stop):
	"""Part one: make a list of dictionaries using range of numbers to be divisible by"""
	count = stop
	rangeList = []
	
	while count >= start:
		rangeList.append(dict({"num":count, "switch":False}))
		count -= 1
	
	"""Part Two: starting from the largest number, multiply in increments of one until all numbers in list divide evenly into product"""
	
	count = 1
	trueCount = 0
	while trueCount < len(rangeList):
		solution = stop * count
		for divisionCheck in rangeList:
			if solution % divisionCheck["num"] == 0:
				divisionCheck["switch"] = True
				trueCount += 1
				
			elif solution % divisionCheck["num"] != 0:
				count += 1
				trueCount = 0
				break
	
	return solution
			
			
	

print(smallestMultiple(1,7))
