document.addEventListener("DOMContentLoaded", function(e) {
	var states = d3.select("svg").selectAll("path")['_groups'];
	info = [1,2,3,4,5,6,7,8,9,10];
	console.log(d3.select("svg").selectAll("path"))

	d3.select("svg").selectAll("path")
		.data(info)
		.style("color", "pink");
	console.log("hi")
})