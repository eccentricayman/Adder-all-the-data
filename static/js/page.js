document.addEventListener("DOMContentLoaded", function(e) {

	var make_test = function(start, stop, step) {
		var ret = [];
		while (start<stop) {
			ret.push(start);
			start += step;
		}
		return ret;
	}

	var get_color = function(percent) {
		 var val = "#00".concat(Math.round(percent*255).toString(16)).concat("00");
		 return val;
	}

	var states = d3.select("svg").selectAll("path")['_groups'];
	info = make_test(0,1,.02)
	console.log(d3.selectAll("path"))

	d3.selectAll("path")
		.data(info)
		.attr("fill", function(d) { return get_color(d); })
})