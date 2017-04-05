var margin = {top: 20, right: 30, bottom: 30, left: 40},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var x = d3.scale.ordinal().rangeRoundBands([0, width], .1);

var y = d3.scale.linear().range([height, 0]);
var nation_data = '{"Drugs": {"2002": {"Rates": {"Alcohol": 2.09, "Illicit Drugs": 2.96, "Marijuana": 15.37},"Sums": {"Alcohol": 518520, "Illicit Drugs": 735060, "Marijuana": 3812160, "Population": 24799277}},"2003": {"Rates": {"Alcohol": 2.05, "Illicit Drugs": 2.89, "Marijuana": 15.15}, "Sums": {"Alcohol": 511600, "Illicit Drugs": 721020, "Marijuana": 3781990, "Population": 24961002}}, "2004": {"Rates": {"Alcohol": 2.01, "Illicit Drugs": 2.81, "Marijuana": 14.93}, "Sums": {"Alcohol": 504550, "Illicit Drugs": 706630, "Marijuana": 3751370, "Population": 25122751}}, "2005": {"Rates": {"Alcohol": 1.97, "Illicit Drugs": 2.74, "Marijuana": 14.71}, "Sums": {"Alcohol": 497500, "Illicit Drugs": 692090, "Marijuana": 3720300, "Population": 25284500}},"2006": {"Rates": {"Alcohol": 1.93, "Illicit Drugs": 2.66, "Marijuana": 14.5}, "Sums": {"Alcohol": 490410, "Illicit Drugs": 677270, "Marijuana": 3688750, "Population": 25446246}}, "2007": {"Rates": {"Alcohol": 1.89, "Illicit Drugs": 2.59, "Marijuana": 14.28}, "Sums": {"Alcohol": 483220, "Illicit Drugs": 662150, "Marijuana": 3656820, "Population": 25607995}}, "2008": {"Rates": {"Alcohol": 1.85, "Illicit Drugs": 2.51, "Marijuana": 14.06}, "Sums": {"Alcohol": 476060, "Illicit Drugs": 646830, "Marijuana": 3624320, "Population": 25769744}}, "2009": {"Rates": {"Alcohol": 1.81, "Illicit Drugs": 2.43, "Marijuana": 13.85}, "Sums": {"Alcohol": 468830, "Illicit Drugs": 631200, "Marijuana": 3591440, "Population": 25931513}}, "2010": {"Rates": {"Alcohol": 1.57, "Illicit Drugs": 2.33, "Marijuana": 13.73}, "Sums": 1234}}}'

var nationalData = JSON.parse(nation_data)
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

