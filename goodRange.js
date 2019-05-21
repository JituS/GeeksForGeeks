process.stdin.resume();
process.stdin.setEncoding("utf-8");
var stdin_input = "";

process.stdin.on("data", function (input) {
    stdin_input += input;
});

process.stdin.on("end", function () {
   main(stdin_input);
});

function main(input) {
	var splitted = input.split('\n');
	var rangeNumber = parseInt(splitted[0].split(' ')[0]);
	var querieCount = parseInt(splitted[0].split(' ')[1]);
	var queries = splitted.slice(1).map(a => parseInt(a));
	for (var i = 1; i <= queries.length; i++) {
		var q = queries.slice(0, i).sort(), sum = 0;
		console.log(q)
		for (var j = q.length-1; j > -1;j--) {
			if (!q[j-1]) sum += 1;
			else sum += q[j-1];
			if (!q[j+1]) sum += rangeNumber;
			else sum += q[j+1];
		}
		console.log(sum);
	}
}
