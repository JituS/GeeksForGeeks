var highestSum = function(input) {
	return Math.max.apply(null, input.reduce(function(pv, cv, index) {
		if (index == 0) return [cv];
		pv.push(Math.max(cv, cv + pv[pv.length  - 1]));
		return pv;
	}, 0));
};

console.log(highestSum([-2, -3, 4, -1, -2, 1, 5, -3]));
