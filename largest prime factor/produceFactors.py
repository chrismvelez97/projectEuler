def factorsList(testNum):
	factors = []

	for iter in range(1,int(testNum) + 1):
		if testNum % iter == 0:
			factors.append(iter)

	#if len(factors) == 2:
	#	print ("This number is a prime")
	
	#else:
		#print("This number is not a prime")
		
	return (factors)
	
#print(factorsList(100))
