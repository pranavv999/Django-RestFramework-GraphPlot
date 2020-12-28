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
    if (object["year_range"]) {
        ApiUrl = `http://localhost:8000/api/problem_four/?country_group=${object['country_group']}&start_year=${object['start_year']}&year_range=${object['year_range']}`

    } else {

        ApiUrl = `http://localhost:8000/api/problem_four/?country_group=${object['country_group']}&start_year=${object['start_year']}`

    }

    // Getting DATA from API URL
    fetch(ApiUrl).then(response => response.json()).then(json => plotGraph(json, object['country_group']));
});

function plotGraph(json, graphTitle) {

    // data will store arry of objects in following form
    // data =[{name:countryName, data:populationList}, {name:countryName, data:populationList}]
    var data = [];
    // Storing unique Year values
    var years = new Set();

    // Creating object in this form {countryName:[populationList]}
    var dict = {};
    var val;
    for (val of json) {
        if (!(val['region'] in dict)) {

            // If key is not present will create key
            dict[val['region']] = [];

        }

        dict[val['region']].push(val['population']);

        // adding years to Set it will store only unique year values
        years.add(val['year']);

    }

    // Populating data array
    for (const key in dict) {
        data.push(
            {
                name: key,
                data: dict[key]
            }
        );
    }

    // Converting yers set to years array
    var yearsList = Array.from(years);

    // Chart Plotting
    Highcharts.chart('container-1', {
        chart: {
            type: 'column',
            height: 500,
        },
        title: {
            text: `${graphTitle} Countries Population For Year ${yearsList[0]} - ${yearsList[yearsList.length - 1]}`
        },
        subtitle: {
            text: 'Source: <a href="https://datahub.io/core/population-growth-estimates-and-projections/r/population-estimates.csv">Population Data</a>'
        },
        xAxis: {
            categories: yearsList,
            title: {
                text: "Years",
                style: {
                    color: '#000',
                    fontSize: '1.5em'
                }
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Population',
                style: {
                    color: '#000',
                    fontSize: '1.5em'
                }
            },
            labels: {
                overflow: 'justify'
            }
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
        series: data
    });


}