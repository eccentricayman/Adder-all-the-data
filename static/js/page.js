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
		if ((percent==0) || (percent==null)) {
			return "#ffffff";
		}
		var val = "#".concat(Math.round(percent*250).toString(16)).concat("ff").concat(Math.round(percent*250).toString(16))
		//console.log(percent.toString().concat("\n").concat(val.toString()).concat("\n"));
		return val;
	}

	$.ajax({
		url: '/corrs/',
		type: 'POST',
		data: {},
		success: function(i){
			var info = JSON.parse(i)
			keys = Object.keys(info)

			var ctr = 0;
			for (ctr=0; ctr<keys.length; ctr++) {
				id = "#" + keys[ctr];
				if (id=="#GA") {
					console.log(info[keys[ctr]])
				}
				d3.selectAll(id)
				.data([info[keys[ctr]]])
				//.attr("fill", function(d) { return get_color(d); })
			}

			d3.selectAll("path")
			.attr("fill", function(d) { 
				return get_color(d);
			})

			d3.select("#path67")
			.attr("fill", "none")
		}
	})
});