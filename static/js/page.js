var nationalData;
var fullSVG;

var map = jQuery.extend(true, {}, originalObject);

document.addEventListener("DOMContentLoaded", function(e) {

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


    $.get( "/nationalData", {}, function(d){
        nationalData = JSON.parse(d)
	nationalKeys = Object.keys(nationalData)
	nationalValues = Object.values(nationalData)

	var us = d3.select("id")//??
	
	var stats = function() {
	    us.selectAll("div")
		.data(values)
		.enter()
		.append("div")
		.style("height", function(i){
		    return i*30 + "px";
		})
		.text( function(a){
		    return a;
		});
	}
	var transitionTest = function( scale ) {
	    us.selectAll("div")
		.data(values)
		.transition()
		.duration(2000)
		.style("height", function(b) {
		    return b * scale + "px";
		});
	};
	
	stats();
	transitionTest();
    });

    var renderData = function(d){
	var info = JSON.parse(d[0])
	stateKeys = Object.keys(info)
	stateValues = Object.values(info)

	for stateName, cde in d[1].items():
        if cde == :
            id = stateName
	var state = d3.select(id)
	
	var stats = function() {
	    state.selectAll("div")
		.data(values)
		.enter()
		.append("div")
		.style("height", function(i){
		    return i*30 + "px";
		})
		.text( function(a){
		    return a;
		});
	}

	var transitionTest = function( scale ) {
	    state.selectAll("div")
		.data(values)
		.transition()
		.duration(2000)
		.style("height", function(b) {
		    return b * scale + "px";
		});
	};
	
	stats();
	transitionTest();
    };

    
});

