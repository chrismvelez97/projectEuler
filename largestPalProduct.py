truePal = 12321
falsePal = 123


def isPal(check):
  listCheck = []
  strCheck = str(check)

  for letter in strCheck:
    listCheck.append(letter)

  firstHalf = listCheck[0:int(len(listCheck) / 2)]

  secondHalf = listCheck[int(len(listCheck) / 2):]

  if len(listCheck) % 2 != 0:
    secondHalf.pop(0)

  print("First Half: ")
  print(firstHalf)

  print("Second Half: ")
  print(secondHalf)

  count = len(secondHalf) - 1
  secReversed = []

  while count >= 0:
    secReversed.append(secondHalf[count])
    count -= 1
  print("SecReversed: ")
  print(secReversed)
  count = 0
  while count < len(firstHalf):
    if firstHalf[count] != secReversed[count]:
      print("Not a palindrome")
      return False

    count += 1
  print("Is a palindrome")
  return True

def largestPalProduct():
	switch = True
	numOne = 999
	numTwo = 999
	
	while isPal(numOne*numTwo) == False:
		if switch == True:
			numOne -= 1
			switch = False
		elif switch == False:
			numTwo -= 1
			switch = True
	return [numOne,numTwo,numOne*numTwo]

print(largestPalProduct())
		
