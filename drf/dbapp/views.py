from django.shortcuts import render

from django.db.models import Sum
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import (PopulationSerializer, ProblemOneSerializer,
                          ProblemThreeSerializer)
from .models import Population, Groupings


# Create your views here.

# Home view
def home(request):
    '''This Function Returns The Home Page of Project'''
    return render(request, 'dbapp/index.html')


# Problem 1 Home View

def problem_one_home(request):
    '''Home Page of Problem One'''
    # Getting unique country names for dropdown
    c = Population.objects.order_by('region').\
        values('region').distinct('region')
    c = [i['region'] for i in c]

    # Getting unique years available for dropdown
    y = Population.objects.order_by('year').\
        values('year').distinct('year')
    y = [int(i['year']) for i in y]

    # Creating Dictionary to send it to template
    context = {
        'country_names': c,
        'years': y
    }
    return render(request, 'dbapp/problem1.html', context)


# Problem 2 Home View

def problem_two_home(request):
    '''Home Page of Problem Two'''
    # Getting unique country_group names for dropdown
    g = Groupings.objects.order_by('group').\
        values('group').distinct('group')
    g = [i['group'] for i in g]

    # Getting unique years available for dropdown
    y = Population.objects.order_by('year').\
        values('year').distinct('year')
    y = [int(i['year']) for i in y]

    # Creating Dictionary to send it to template
    context = {
        'country_group': g,
        'years': y
    }
    return render(request, 'dbapp/problem2.html', context)


# Problem 3 Home View

def problem_three_home(request):
    '''Home Page of Problem Three'''
    # Getting unique country_group names for dropdown
    g = Groupings.objects.order_by('group').\
        values('group').distinct('group')
    g = [i['group'] for i in g]

    # Getting unique years available for dropdown
    y = Population.objects.order_by('year').\
        values('year').distinct('year')
    y = [int(i['year']) for i in y]

    # Creating Dictionary to send it to template
    context = {
        'country_group': g,
        'years': y
    }
    return render(request, 'dbapp/problem3.html', context)


# Problem 4 Home View

def problem_four_home(request):
    '''Home Page of Problem Four'''
    # Getting unique country_group names for dropdown
    g = Groupings.objects.order_by('group').\
        values('group').distinct('group')
    g = [i['group'] for i in g]

    # Getting unique years available for dropdown
    y = Population.objects.order_by('year').\
        values('year').distinct('year')
    y = [int(i['year']) for i in y]

    # Creating Dictionary to send it to template
    context = {
        'country_group': g,
        'years': y
    }
    return render(request, 'dbapp/problem4.html', context)


# API views


@api_view(['GET'])
def api_list(request):
    '''This is just a API Overview'''
    population = Population.objects.all()[0:30]
    serializer = PopulationSerializer(population, many=True)

    return Response(serializer.data)


# Problem 1 API
@api_view(['GET', 'POST'])
def problem_one(request):
    '''This API will give us the data in following form
    {
        "region": "Region-Name",
        "year": year,
        "population": population-count
    }
    For selected Country, Start_year  and year Range.

    If you Specify the Region-name, Start-year and Range in the Post form like

    {
        "region" : "Nepal",
        "start_year" : "2000",
        "year_range" : "10"
    }

    you will get the data in JSON format for specified query
    '''
    if request.method == 'GET':
        region = request.query_params.get('region', 'India')
        start_year = int(request.query_params.get('start_year', '2004'))
        year_range = int(request.query_params.get('year_range', '10'))
        end_year = ((start_year + year_range) if
                    ((start_year + year_range) <= 2015) else 2015)

        year_range = [i for i in range(start_year, end_year + 1)]
        # Datbase Query
        population_data = Population.objects.filter(
            region__exact=region,
            year__in=year_range
        )
        serializer = ProblemOneSerializer(population_data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        region = request.data.get('region', 'India')
        start_year = int(request.data.get('start_year', '2004'))
        year_range = int(request.data.get('year_range', '10'))
        end_year = ((start_year + year_range) if
                    ((start_year + year_range) <= 2015) else 2015)

        year_range = [i for i in range(start_year, end_year + 1)]
        # Datbase Query
        population_data = Population.objects.filter(
            region__exact=region,
            year__in=year_range
        )
        serializer = ProblemOneSerializer(population_data, many=True)
        return Response(serializer.data)


# Problem 2 API
@api_view(['GET', 'POST'])
def problem_two(request):
    '''This API will give us the data in following form
    {
        "region": "Region-Name",
        "year": year,
        "population": population-count
    }
    for Selected Country_Grouping and Start year.

    If you Specify the Country-grouping, Start-year in Post form like

    {
    "country_group" : "G5",
    "year" : "2001"
    }

    you will get the data in JSON format for specified query
    '''
    if request.method == "GET":
        country_group = request.query_params.get('country_group', 'Asean')
        year = int(request.query_params.get('start_year', '2014'))
        g = Groupings.objects.filter(group__exact=country_group)[0]
        g = g.countries.filter(year__exact=year)
        serializer = ProblemOneSerializer(g, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        country_group = request.data.get('country_group', 'Asean')
        year = int(request.data.get('start_year', '2014'))
        g = Groupings.objects.filter(
            group__exact=country_group
        ).first().countries.filter(year__exact=year)
        # g = g.countries.filter(year__exact=year)
        serializer = ProblemOneSerializer(g, many=True)
        return Response(serializer.data)


# Problem 3 API
@api_view(['GET', 'POST'])
def problem_three(request):
    '''This API will give us the data in following form
    {
        "year": Year,
        "total_population": population_data
    }
    for Selected Country_Grouping and Start year and Range.

    If you Specify the Country-grouping, Start-year & Range in the
Post form like

    {
    "country_group" : "G4",
    "start_year" : "2000",
    "year_range" : "10"
    }

    you will get the data in JSON format for specified query
    '''
    if request.method == "GET":
        country_group = request.query_params.get('country_group', 'Saarc')
        start_year = int(request.query_params.get('start_year', '2004'))
        year_range = int(request.query_params.get('year_range', '10'))
        end_year = ((start_year + year_range) if
                    ((start_year + year_range) <= 2015) else 2015)
        # Database query

        # 1 Pulling Country group from table
        g = Groupings.objects.filter(
            group__exact=country_group
        ).first()

        # 2 Filtering for required year
        g = g.countries.filter(
            year__gte=start_year,
            year__lte=end_year
        )

        # 3 Grouping by year to do sum for that year for entire group
        g = g.values('year').order_by('year').annotate(
            total_population=Sum('population')
        )

        # Serializing data
        serializer = ProblemThreeSerializer(g, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        country_group = request.data.get('country_group', 'Saarc')
        start_year = int(request.data.get('start_year', '2004'))
        year_range = int(request.data.get('year_range', '10'))
        end_year = ((start_year + year_range) if
                    ((start_year + year_range) <= 2015) else 2015)

        # Database query

        # 1 Pulling Country group from table
        g = Groupings.objects.filter(
            group__exact=country_group
        ).first()

        # 2 Filtering for required year
        g = g.countries.filter(
            year__gte=start_year,
            year__lte=end_year
        )

        # 3 Grouping by year to do sum for that year for entire group
        g = g.values('year').order_by('year').annotate(
            total_population=Sum('population')
        )

        # Serializing data
        serializer = ProblemThreeSerializer(g, many=True)
        return Response(serializer.data)


# Problem 4 API
@api_view(['GET', 'POST'])
def problem_fourth(request):
    '''This API will give us the data in following form
    {
        "region": "Region_name",
        "year": Year,
        "population": Population_count
    }
    for Selected Country_Grouping and Start year and Range.

    If you Specify the Country-grouping, Start-year & Range in the
Post form like

    {
    "country_group" : "G4",
    "start_year" : "2000",
    "year_range" : "10"
    }

    you will get the data in JSON format for specified query
    '''
    if request.method == "GET":
        country_group = request.query_params.get('country_group', 'Asean')
        start_year = int(request.query_params.get('start_year', '2004'))
        year_range = int(request.query_params.get('year_range', '10'))
        end_year = ((start_year + year_range) if
                    ((start_year + year_range) <= 2015) else 2015)

        # Database query
        # 1 Pulling Country group from table
        g = Groupings.objects.filter(
            group__exact=country_group
        ).first()

        # 2 Filtering for required year
        g = g.countries.filter(
            year__gte=start_year,
            year__lte=end_year
        )

        # Ordering by year
        g = g.order_by('year')

        # Serializing Data
        serializer = ProblemOneSerializer(g, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        country_group = request.data.get('country_group', 'Asean')
        start_year = int(request.data.get('start_year', '2004'))
        year_range = int(request.data.get('year_range', '10'))
        end_year = ((start_year + year_range) if
                    ((start_year + year_range) <= 2015) else 2015)

        # Database query
        # 1 Pulling Country group from table
        g = Groupings.objects.filter(
            group__exact=country_group
        ).first()

        # 2 Filtering for required year
        g = g.countries.filter(
            year__gte=start_year,
            year__lte=end_year
        )

        # Ordering by year
        g = g.order_by('year')

        # Serializing Data
        serializer = ProblemOneSerializer(g, many=True)
        return Response(serializer.data)
