var nationalData;
var stateData;
var states;
var xmlns = "http://www.w3.org/2000/svg"

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

    $.get( "/nationalData/", {}, function(d){
        nationalData = JSON.parse(d)
    });

    //renderUS();
    
    states = document.getElementById('g5').children
    for( i =0; i < states.length; i++){
        if( states[i].getAttribute('id') != 'GA' && states[i].getAttribute('id') != 'DC' ){
            states[i].addEventListener( "click", render ); 
        };
    };
    
});


var render = function(){

    console.log(nationalData);
    
    //Loop through all the states, hiding them one by one
    for( i=0; i < states.length; i++){
        if( states[i].getAttribute('id') != this.getAttribute('id') ){
            states[i].setAttribute("display", "none"); 
        };
    }

    //Also hide path67 + path58
    document.getElementById('path67').setAttribute("display", "none")
    document.getElementById('path58').setAttribute("display", "none")

    //Remove current eventListener
    this.removeEventListener("click", render )

    //Add new eventListener
    this.addEventListener("click", reset )

    //Calculate Transformation
    var trans = function(e){
        //First get Origin Point ( prob not the most accurate point to use. W/e )
        var coords = e.getAttribute("d").split("l")[0].substring(1).split(',')//Get Rid of the M. I don't need it :D

        console.log(e.getBoundingClientRect())

        var X = Number(e.pageX); 
        var Y = Number(e.pageY);
        
        var finalX = 100 // AYMAN *READ THIS*
        var finalY = 100 // THESE COORDS ARE WHERE THE STATE WILL END UP. CHANGE AS NEED BE
        
        return "translate("+(finalX - X + 200)+","+(finalY - Y + 100)+")";
    };

    var transform = trans(this);
    console.log(transform)
    //Move the state into proper spot. Also, add a Text Tag
    this.setAttribute("transform", transform );
    var svg = document.getElementById('us-map');
    var textBox = document.createElementNS(xmlns, "text");
    textBox.innerHTML = this.getAttribute("data-info");
    textBox.setAttribute("x", 200)
    textBox.setAttribute("y", 100)
    //textBox.setAttribute("x")
    svg.appendChild( textBox );

    $.get( "/stateData/<state>", {}, function(d){
	stateData = JSON.parse(d)
    });
    
    renderData()
    renderUS();
}


var reset = function(){

    //Loop through all the states, hiding them one by one
    for( i=0; i < states.length; i++){
        if( states[i].getAttribute('id') != this.getAttribute('id') ){
            states[i].setAttribute("display", "initial"); 
        };
    }

    //Also hide path67 + path58
    document.getElementById('path67').setAttribute("display", "initial")
    document.getElementById('path58').setAttribute("display", "initial")

    //Remove current eventListener
    this.removeEventListener("click", reset )

    //Add new eventListener
    this.addEventListener("click", render )

    //undo Transformation
    this.removeAttribute("transform")
    
}


var renderUS = function(){
    console.log(nationalData)
    var nationalKeys = Object.keys(nationalData)
    //console.log(nationalData['Drugs'])
    var years = Object.keys(nationalData['Drugs'])
    //console.log(years)

    var get_values = function(year){
	values = Object.values(nationalData['Drugs'][year]['Rates'])
	return values;
    }

    //console.log(get_values('2002'))
    var renderNation = function(y, year, scale){
	var us = d3.select(y)

	us.selectAll("div")
	    .data(get_values(year))
	    .enter()
	    .append("div")
	    .transition()
	    .duration(2000)
	    .style("width", function(i){
		//console.log(i*scale + " px")
		return i*scale + "px";
	    })
	    .text( function(a){
		return a;
	    });
    };

    renderNation(y2,2002,25);
    renderNation(y3,2003,25);
    renderNation(y4,2004,25);
    renderNation(y5,2005,25);
    renderNation(y6,2006,25);
    renderNation(y7,2007,25);
    renderNation(y8,2008,25);
    renderNation(y9,2009,25);
    renderNation(y10,2010,25);
}

//renderUS();


var renderData = function(d){
    var info = JSON.parse(d)
    var stateKeys = Object.keys(info)
    var stateValues = Object.values(info)

    //for stateName, cde in d[1].items():
    //if cde == :
    //id = stateName

    var stats = function(y, year, scale){
	var state = d3.select(y)

	us.selectAll("div")
	    .data(get_values(year))
	    .enter()
	    .append("div")
	    .transition()
	    .duration(2000)
	    .style("width", function(i){
		//console.log(i*scale + " px")
		return i*scale + "px";
	    })
	    .text( function(a){
		return a;
	    });
    };
    
    stats(s2,2002,25);
};

