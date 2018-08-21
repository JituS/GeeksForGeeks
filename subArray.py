def subArray(numbers, sum):
	for i, value in enumerate(numbers):
		for j in range(i-1, -1, -1):
			value += numbers[j]
			if value == sum:
				return str(j+1) + " " + str(i+1)
	return -1

for x in range(int(input())):
	numberCount, sum = [ int(i) for i in input().split() ]
	numbers = [ int(i) for i in input().split() ]
	print(subArray(numbers, sum))
