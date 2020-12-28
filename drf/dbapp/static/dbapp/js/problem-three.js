document.getElementById('myform').addEventListener('submit', (event) => {

    // Preventing submit button refresh behaviour
    event.preventDefault();
    const formData = new FormData(event.target);

    var object = {};
    formData.forEach(function (value, key) {
        object[key] = value;
    });


    // Creating Url based on selected range value if range is not selected default is 10
    var ApiUrl;
    if (object["year_range"]){
        ApiUrl = `http://localhost:8000/api/problem_three/?country_group=${object['country_group']}&start_year=${object['start_year']}&year_range=${object['year_range']}`

    } else {

        ApiUrl = `http://localhost:8000/api/problem_three/?country_group=${object['country_group']}&start_year=${object['start_year']}`

    }


    // Getting DATA from API URL
    fetch(ApiUrl).then(response => response.json()).then(json => plotGraph(json, object['country_group']));
});

function plotGraph(json, graphTitle) {
    var data = [];
    var years = [];
    // json[0]['region']
    for (object of json) {
        data.push(object['total_population']);
        years.push(object['year']);

    };


    Highcharts.chart('container-1', {
        chart: {
            type: 'column',
            height: 500,
        },
        title: {
            text: `${graphTitle} Population For Year ${years[0]} to ${years[data.length - 1]
        }`
        },
        subtitle: {
            text: 'Source: <a href="https://datahub.io/core/population-growth-estimates-and-projections/r/population-estimates.csv">Population Data</a>'
        },
        xAxis: {
            categories: years,
            title: {
                text: 'Years',
                style: {
                    color: '#ff7d04',
                    fontSize: '1.5em'
                }

            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Population',
                style: {
                    color: '#ff7d04',
                    fontSize: '1.5em'
                }
            },
            labels: {
                overflow: 'justify'
            }
        },
        legend: {
            enabled: false
        },
        credits: {
            enabled: false
        },
        series: [{
            name:"",
            data: data}],
    });

}