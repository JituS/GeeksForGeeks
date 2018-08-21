function maximumSum(subArray, number) {
	for (var i = 0; i < subArray.length; i++) {
		var sum = subArray[i];
		for (var j = i-1; j >= 0; j--) {
			sum += subArray[j];
			if (sum == number) return [j+1, i+1];
		}
	}
	return -1
}

console.log(maximumSum([1,2,3,7,5], 12));
