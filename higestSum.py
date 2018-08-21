# /Library/Frameworks/Python.framework/Versions/3.6/bin/python3
from functools import reduce

def redFunc(pv, cv):
	if len(pv) == 0:
		return [cv]
	pv.append(max(cv, cv + pv[-1]))
	return pv

for x in range(int(input())):
	numberCount = input()
	numbers = [ int(i) for i in input().split() ]
	print(max(reduce(redFunc, numbers, [])))
		

