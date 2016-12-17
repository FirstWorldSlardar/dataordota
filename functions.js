function setGraphOptions(typeName, parsed_data){
	var chart = document.getElementById('chart');
	var myChart = echarts.init(chart);
			
	var level = ["10", "15","20","25"];

	print(parsed_data);
	var heroes = parsed_data['heroes'];
	var data = parsed_data['data'];

	var option = {
	    title: {
	        text: 'Distribution des talents par '+ typeName,
	        link: 'http://www.dota2.com/700/gameplay/'
	    },
	  
	    polar: {},
	    // ce qui est affiché en y passant la souris
	    tooltip: {
	    	// params.value[] est un element de data = [x,y,z]
	        formatter: function (params) {
	            return params.value[2]+ " " + typeName+ " at Level  " + level[params.value[0]]+ " -"+heroes[params.value[1]];
	        }
	    },
	    angleAxis: {
	        type: 'category',
	        data: heroes,
	        boundaryGap: false,
	        splitLine: {
	            show: true,
	            lineStyle: {
	                color: '#999',
	                type: 'dashed',
	            }
	        },
	        axisLine: {
	            show: false
	        }
	    },
	    radiusAxis: {
	        type: 'category',
	        data: level,
	        axisLine: {
	            show: false
	        },
	        axisLabel: {
	            rotate: 45
	        }
	    },
	    series: [{
	        name: 'Punch Card',
	        type: 'scatter',
	        coordinateSystem: 'polar',
	        symbolSize: function (val) {
	            return val[2] * 0.39;
	        },
	        data: data,
	        animationDelay: function (idx) {
	            return idx * 5;
	        }
	    }]
	};

	myChart.setOption(option);
}

function insertOption(talentType){
		var newOption = document.createElement('option');
		newOption.setAttribute('value', talentType);
		newOption.innerHTML = talentType;
		document.getElementById("selection").appendChild(newOption);
}