from produceFactors import factorsList as fl

num = input("Give Number:\n\n")
def producePrimeList(num):
	list = fl(int(num))
	primeList = []
	for number in list:
		if len(fl(int(number))) <= 2:
			primeList.append(number)
	return (primeList)

def largestPrimeFactor(num):
	list = producePrimeList(num)
	return (list[len(list)-1])

print(largestPrimeFactor(num))

