function longestSubsequence(numbers) {
	var result = 0;
	numbers.reduce(function(pv, cv) {
		if (pv.length == 0) {
			result = 1;
			return [{value: cv, maxForThis: 1}];
		}
		var max = 1;
		pv.forEach(function(each) {
			if (each.value < cv) {
				if (each.maxForThis + 1 > max) max = each.maxForThis + 1;
			}
		});
		pv.push({value: cv, maxForThis: max});
		if (result < max) result = max;
		return pv;
	}, []);
	return result;
}

console.log(longestSubsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
