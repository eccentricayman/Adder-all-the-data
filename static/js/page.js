//first animation
$(".animation-wrapper").fadeIn(1500);

var nationalData;
var stateData;

$.get( "/nationalData/", {}, function(d){
    nationalData = JSON.parse(d);
});

var states;
var state;
var xmlns = "http://www.w3.org/2000/svg";

var map = document.getElementById("clone").cloneNode(true);
var defaultTable = document.getElementById("table-data").cloneNode(true);

$("#table-data").css('display', 'none');

var renderColor = function(e) {
    
    var get_color = function(percent) {
	    if ((percent === 0) || (percent === null)) {
	        return "#ffffff";
	    }
	    var val = "#".concat(Math.round(percent*250).toString(16)).concat("ff").concat(Math.round(percent*250).toString(16));
	    //console.log(percent.toString().concat("\n").concat(val.toString()).concat("\n"));
	    return val;
    };

    $.ajax({
	    url: '/corrs/',
	    type: 'POST',
	    data: {},
	    success: function(i){
	        var info = JSON.parse(i);
	        keys = Object.keys(info);

	        var ctr = 0;
	        for (ctr=0; ctr<keys.length; ctr++) {
		        id = "#" + keys[ctr];
		        if (id=="#GA") {
		            console.log(info[keys[ctr]]);
		        }
		        d3.selectAll(id)
		            .data([info[keys[ctr]]]);
		        //.attr("fill", function(d) { return get_color(d); })
	        }

	        d3.selectAll("path")
		        .attr("fill", function(d) { 
		            return get_color(d);
		        });

	        d3.select("#path67")
		        .attr("fill", "none");
	    }
    });
    
    //renderUS();
    
    states = document.getElementById('g5').children;
    for( i =0; i < states.length; i++){
        if( states[i].getAttribute('id') != 'GA' && states[i].getAttribute('id') != 'DC' ){
            states[i].addEventListener( "click", render ); 
        }
    }
    
};

document.addEventListener("DOMContentLoaded", renderColor);

var render = function(e) {

    //console.log(nationalData);

    //we are removing map entirely, then adding state we want to new svg
    g5 = document.getElementById("g5");
    var currentState;

    while (g5.lastElementChild) {
        if( g5.lastElementChild.getAttribute('id') != e.srcElement.getAttribute('id') ) {
            g5.removeChild(g5.lastElementChild);
        }
        else {
            currentState = g5.lastElementChild.cloneNode(true);
            g5.removeChild(g5.lastElementChild);
        }
    }
    var svgRemover = document.getElementById("clone").parentNode;
    svgRemover.removeChild(document.getElementById("clone"));

    //adding h1
    var stateHeading = document.createElement("h1");
    stateHeading.id = "state-heading";
    stateHeading.innerHTML = currentState.getAttribute('data-info');
    svgRemover.prepend(stateHeading);
    
    var svgAdder = svgRemover.prepend(document.createElementNS(xmlns, "svg"));
    //only one svg
    $("svg").attr("id", "state");

    var svg = document.getElementById("state");
    svg.appendChild(currentState);

    //height 100, scale box
    var bbox = currentState.getBBox();
    currentState.setAttribute("transform", "scale(" + (200.0 / bbox.y) + ")");

    /////////////////////////////////////////////////////////////////
    // KEVIN FIX THIS, BBOX DOESNT WANNA RESCALE, this doesnt work //
    /////////////////////////////////////////////////////////////////
    
    //get smaller scaled bbox
    bbox = currentState.getBBox();

    //set svg size to new state size
    svg.setAttribute("width", bbox.x);
    svg.setAttribute("height", 200);

    //add translate to the scale, and mvoe to top left
    var transform = currentState.getAttribute("transform") + ',translate(' + (-1 * bbox.x) + "," + (-1 * bbox.y) + ")";
    currentState.setAttribute("transform", transform);

    ///////////////////////////////////////////////////////
    // KEVIN UNCOMMENT THE BELOW ONCE YOU GET IT WORKING //
    ///////////////////////////////////////////////////////
    
    //move h1 next to state
    // bbox = currentState.getBBox();
    // stateHeading.style.top = (bbox.y / 5.0) + "px";
    // stateHeading.style.left = bbox.x + 25 + "px";
    
    //temp til it works (above)
    stateHeading.style.right = 0;
    stateHeading.style.top = 0;
    stateHeading.style['margin-right'] = "1%";
    
    //Remove current eventListener
    currentState.removeEventListener("click", render);

    //Add new eventListener
    currentState.addEventListener("click", reset);

    //table hide and reveal
    $("#table-data").css("display", "block");

    //kevins calculations
    // //Calculate Transformation
    // var trans = function(e){
    //     //First get Origin Point ( prob not the most accurate point to use. W/e )
    //     var coords = e.getAttribute("d").split("l")[0].substring(1).split(',');//Get Rid of the M. I don't need it :D

    //     console.log(e.getBoundingClientRect());
    //     var X = Number(e.pageX); 
    //     var Y = Number(e.pageY);
    
    //     var finalX = 100; // AYMAN *READ THIS*
    //     var finalY = 100; // THESE COORDS ARE WHERE THE STATE WILL END UP. CHANGE AS NEED BE
    
    //     return "translate("+(finalX - X + 200)+","+(finalY - Y + 100)+")";
    // };

    // var transform = trans(this);
    // console.log(transform);
    // //Move the state into proper spot. Also, add a Text Tag
    // this.setAttribute("transform", transform );
    // var svg = document.getElementById('us-map');
    // var textBox = document.createElementNS(xmlns, "text");
    // textBox.innerHTML = this.getAttribute("data-info");
    // textBox.setAttribute("x", 200);
    // textBox.setAttribute("y", 100);
    // //textBox.setAttribute("x")
    // svg.appendChild( textBox );
    
    
    /*
      $.get( "/stateData/<state>", {}, function(d){
      stateData = JSON.parse(d[0])
	  states = d[1]
	  state = d[2]
      });
    */

    var renderUS = function(){
        console.log(nationalData)
        var nationalKeys = Object.keys(nationalData)
        //console.log(nationalData);
        //console.log(nationalData['Drugs'])
        var years = Object.keys(nationalData['Drugs']);
        //console.log(years)

        var get_drug_values = function(year){
	        values = Object.values(nationalData['Drugs'][year]['Rates'])
	        return values;
        }
        var get_score_values = function(year){
	        values = Object.values(nationalData['Scores'][year]['Averages'])
	        return values;
        }

        //console.log(Object.keys(nationalData['Drugs']['2006']['Rates']))

        //console.log(get_values('2002'))
        var renderDrugs = function(y, year, scale){
	        var us = d3.select(y)

	        us.selectAll("div")
	            .data(get_drug_values(year))
	            .enter()
	            .append("div")
	            .transition()
	            .duration(2000)
	            .style("width", function(i){
		            //console.log(i*scale + " px")
		            return i*scale + "px";
	            })
	            .text( function(a){
		            var t = a;
		            var drug;
		            for (drug in nationalData['Drugs'][year]['Rates']){
		                //console.log(drug)
		                //console.log(nationalData['Drugs'][year]['Rates'][drug])
		                if (nationalData['Drugs'][year]['Rates'][drug] == a){
			                console.log(a)
			                t = drug+":"+a;
		                }
		            }
		            return t;
	            });
        };

        var renderScores = function(y, year, scale, scale2){
	        var us = d3.select(y)

	        us.selectAll("div")
	            .data(get_score_values(year))
	            .enter()
	            .append("div")
	            .transition()
	            .duration(2000)
	            .style("width", function(i){
		            var s = i;
		            if (i < 5){
		                s = s*15
		            }
		            //console.log(i*scale + " px")
                    if (s > 500) {
                        return (s * scale2) + "px";
                    }
                    else {
		                return s*scale + "px";
                    }
	            })
	            .text( function(a){
		            for (s in nationalData['Scores'][year]['Averages']){
		                if (nationalData['Scores'][year]['Averages'][s] == a){
			                return s+":"+a;
		                }
		            }
		            return a;
	            });
        };
        
        //renderDrugs(y2,2002,25);
        //renderDrugs(y3,2003,25);
        //renderDrugs(y4,2004,25);
        //renderDrugs(y5,2005,25);
        
        renderDrugs(y6,2006,30);
        renderDrugs(y7,2007,30);
        renderDrugs(y8,2008,30);
        renderDrugs(y9,2009,30);
        renderDrugs(y10,2010,30);
        renderScores(sc6,2006,2, 0.5);
        renderScores(sc7,2007,2, 0.5);
        renderScores(sc8,2008,2, 0.5);
        renderScores(sc9,2009,2, 0.5);
        renderScores(sc10,2010,2, 0.5);
        
    };


    //renderUS();

    var renderData = function(s){

        setTimeout(console.log('timeout'), 1000);
        
        console.log(stateData);        
        
        var stateKeys = Object.keys(stateData);
        var stateValues = Object.values(stateData);
        
        var convert_state = function(state){
	        for (stateName in states){
	            if (states[stateName]==state){
		            return stateName
	            }
	        }
        }
        
        var get_drug_values = function(year){
            values = Object.values(stateData['Drugs'][year]['Rates'])
	        return values;
        }
        var get_score_values = function(year){
	        values = Object.values(nationalData['Scores'][year]['Averages'])
	        return values;
        }
        
        var renderDrugs = function(y, year, scale){
	        var us = d3.select(y)
            
	        us.selectAll("div")
	            .data(get_drug_values(year))
	            .enter()
	            .append("div")
	            .transition()
	            .duration(2000)
	            .style("width", function(i){
		            //console.log(i*scale + " px")
		            return i*scale + "px";
	            })
	            .text( function(a){
		            var t = a;
		            var drug;
		            for (drug in nationalData['Drugs'][year]['Rates']){
		                //console.log(drug)
		                //console.log(nationalData['Drugs'][year]['Rates'][drug])
		                if (nationalData['Drugs'][year]['Rates'][drug] == a){
			                console.log(a)
			                t = drug+":"+a;
		                }
		            }
		            return t;
	            });
        };
        
        var renderScores = function(y, year, scale, scale2){
	        var us = d3.select(y)
            
	        us.selectAll("div")
	            .data(get_score_values(year))
	            .enter()
	            .append("div")
	            .transition()
	            .duration(2000)
	            .style("width", function(i){
		            var s = i;
		            if (i < 5){
		                s = s*15
		            }
		            //console.log(i*scale + " px")
                    if (s > 500) {
                        return s*scale2 + "px";
                    }
                    else {
		                return s*scale + "px";
                    }
	            })
	            .text( function(a){
		            for (s in nationalData['Scores'][year]['Averages']){
		                if (nationalData['Scores'][year]['Averages'][s] == a){
			                return s+":"+a;
		                }
		            }
		            return a;
	            });
        };
        
        renderDrugs(s6,2006,30);
        renderDrugs(s7,2007,30);
        renderDrugs(s8,2008,30);
        renderDrugs(s9,2009,30);
        renderDrugs(s10,2010,30);
        renderScores(st6,2006,2, 0.5);
        renderScores(st7,2007,2, 0.5);
        renderScores(st8,2008,2, 0.5);
        renderScores(st9,2009,2, 0.5);
        renderScores(st10,2010,2, 0.5);
        
    };

    var s = this.getAttribute('id');
    
    $.get("/stateData/", {'state': s}, function(d){
        stateData = JSON.parse(d);
        renderData(s);
        renderUS();
        
    });
};

var reset = function(){

    //readd old map
    $("body").prepend(map);

    //re deep copy maperino
    map = document.getElementById("clone").cloneNode(true);

    //delete state
    document.getElementById("state").parentNode.removeChild(document.getElementById("state"));
    
    //remove new heading
    document.getElementById("state-heading").parentNode.removeChild(document.getElementById("state-heading"));


    //map doesnt wanna animate in second time around, ah well
    $(".animation-wrapper").css("opacity", 1);
    renderColor();

    //hide table on reset
    document.getElementById("table-data").parentNode.removeChild(document.getElementById("table-data"));
    $("body").append(defaultTable);
    defaultTable = defaultTable.cloneNode(true);

    $("#table-data").css("display", "none");
    // //Loop through all the states, hiding them one by one
    // for( i=0; i < states.length; i++){
    //     if( states[i].getAttribute('id') != this.getAttribute('id') ){
    //         states[i].setAttribute("display", "initial"); 
    //     }
    // }

    // //Also hide path67 + path58
    // document.getElementById('path67').setAttribute("display", "initial");
    // document.getElementById('path58').setAttribute("display", "initial");

    //Remove current eventListener
    this.removeEventListener("click", reset);

};



