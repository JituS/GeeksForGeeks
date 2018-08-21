# from math import floor
# from math import ceil
# def findClosestPalindrome(number):
# 	if len(number) % 2 == 0:
# 		halfNumberLength = int(len(number) / 2)
# 		halfNewNumber = number[:halfNumberLength]
# 		newNumber1 = halfNewNumber + halfNewNumber[::-1]
# 		newNumber2 = str(int(halfNewNumber) - 1) + str(int(halfNewNumber) - 1)[::-1]
# 		return int(newNumber1) if abs((int(newNumber1) - int(number))) < abs((int(newNumber2) - int(number))) else int(newNumber2)
# 	else:
# 		halfNumberLength = ceil(len(number) / 2)
# 		halfNewNumber = number[:halfNumberLength]
# 		newNumber1 = halfNewNumber + halfNewNumber[:-1][::-1]
# 		newNumber2 = str(int(halfNewNumber) - 1) + str(int(halfNewNumber) - 1)[:-1][::-1]
# 		return int(newNumber1) if abs((int(newNumber1) - int(number))) < abs((int(newNumber2) - int(number))) else int(newNumber2)


# for x in input():
# 	number = input()
# 	print(findClosestPalindrome(number))



from math import floor
from math import ceil

def func(closestPalindrome):
	return abs(int(closestPalindrome) - int(number))

def findClosestPalindrome(number):
	halfNewNumber = number[:ceil(len(number) / 2)]
	stringToBeAppended = len(halfNewNumber) if len(number) % 2 == 0 else -1
	newNumber1 = halfNewNumber + halfNewNumber[:stringToBeAppended][::-1]
	newNumber2 = str(int(halfNewNumber) - 1) + str(int(halfNewNumber) - 1)[:stringToBeAppended][::-1]
	newNumber3 = str(int(halfNewNumber) + 1) + str(int(halfNewNumber) + 1)[:stringToBeAppended][::-1]
	prossibleResults = [newNumber1, newNumber2, newNumber3]
	prossibleResults.sort()
	return min(prossibleResults, key=func)

for x in range(int(input())):
	number = int(input())
	if number > 0:
		print(findClosestPalindrome(str(number)))
		continue
	print(0)
