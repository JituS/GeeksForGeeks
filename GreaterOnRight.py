def greaterOnRight(numbers):
	numbers[-1], maxValue = -1, numbers[-1]
	for i in range(len(numbers) -2, -1, -1):
		numbers[i], maxValue = maxValue, max(maxValue, numbers[i])
	return numbers

for x in range(int(input())):
	numberCount = input()
	print(" ".join(map(str, greaterOnRight(list(map(int, input().split()))))))
