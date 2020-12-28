document.getElementById('myform').addEventListener('submit', (event) => {

    // Preventing submit button refresh behaviour
    event.preventDefault(); 
    const formData = new FormData(event.target);

    // getting form values in Dictionery
    var object = {};
    formData.forEach(function (value, key) {
        object[key] = value;
    });

    // Creating API URL
    let ApiUrl = `http://localhost:8000/api/problem_two/?country_group=${object['country_group']}&start_year=${object['start_year']}`

    // Getting DATA from API URL
    fetch(ApiUrl).then(response => response.json()).then(json => plotGraph(json, object['country_group']));
});

// Plot Function
function plotGraph(json, graphTitle) {

    // Extracting json data into suitable format using for loop
    var year;
    var data = [];
    var countries = [];
    for (var val of json) {
        year = val['year'];
        data.push(val['population']);
        countries.push(val['region']);

    };

    // Highcharts plot
    Highcharts.chart('container-1', {
        chart: {
            type: 'column',
            height: 500,
        },
        title: {
            text: `${graphTitle} Countries Population For Year ${year}`
        },
        subtitle: {
            text: 'Source: <a href="https://datahub.io/core/population-growth-estimates-and-projections/r/population-estimates.csv">Population Data</a>'
        },
        xAxis: {
            categories: countries,
            title: {
                text: "Countries",
                style: {
                    color: '#ff7d04',
                    fontSize: '1.5em'
                }
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: "Population",
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
        plotOptions: {
            bar: {
                dataLabels: {
                    enabled: true
                }
            }
        },
        credits: {
            enabled: false
        },
        series: [{
            name: "ASEA",
            data: data
        }],
    });

}