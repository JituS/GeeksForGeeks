def longestSubsequence(numbers):
	maxArray = [i for i in range(len(numbers))]
	for i, value in enumerate(numbers):
		maxArray[0] = 1
		maxValue = 1
		for j in range(0, i):
			if numbers[j] < value and maxValue < maxArray[j] + 1:
				maxValue = maxArray[j] + 1
		maxArray[i] = maxValue
		print(maxArray)
	return 0 if len(maxArray) == 0 else max(maxArray);

for x in range(int(input())):
	numberCount = input()
	numbers = [ int(i) for i in input().split() ]
	print(longestSubsequence(numbers))
