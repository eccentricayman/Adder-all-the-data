document.addEventListener("DOMContentLoaded", function(e) {
	//states = document.getElementsByTagName("path");
	info = [1,2,3,4];
	d3.selectAll("path").data(info)
	d3.selectAll("path").text(function(d) { return d; })
})