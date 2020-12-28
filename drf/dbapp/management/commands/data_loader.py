from django.core.management.base import BaseCommand
import csv
import os
from dbapp.models import (Population, Groupings)
from tqdm import tqdm

ASEAN = [
    "Brunei",
    "Cambodia",
    "Indonesia",
    "Laos",
    "Malaysia",
    "Myanmar",
    "Philippines",
    "Singapore",
    "Thailand",
    "Vietnam",
]

SAARC = [
    "Afghanistan",
    "Bangladesh",
    "Bhutan",
    "India",
    "Maldives",
    "Nepal",
    "Pakistan",
    "Sri Lanka",
]

BRICS = [
    'Brazil',
    'China',
    'India',
    'Russia',
    'South Africa',

]

G_four = [
    'Brazil',
    'Germany',
    'India',
    'Japan',
]

G_five = [
    'Brazil',
    'China',
    'India',
    'Russia',
    'Mexico',
]

# Temporary container
c_code = set()
pops = list()


class Command(BaseCommand):
    help = 'Load data from population.csv file into dtatbase'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **kwargs):
        file_name = kwargs['path']
        print(file_name)
        os.chdir('..')
        fpath = os.getcwd()
        fpath = os.path.join(fpath, file_name)
        try:
            file_name = kwargs['path']
            if file_name[-1:-5:-1][::-1] != '.csv':
                raise FileNotFoundError('File not found')

            with open(fpath, 'r') as csv_file:
                print('inside with')
                csv_reader = csv.DictReader(csv_file)

                a = Groupings(group='Asean')
                a.save()
                s = Groupings(group='Saarc')
                s.save()
                b = Groupings(group='Brics')
                b.save()
                g_four = Groupings(group='G4')
                g_four.save()
                g_five = Groupings(group='G5')
                g_five.save()

                for row in tqdm(
                    csv_reader,
                    total=18018,
                    disable=False,
                    desc="Loading",
                    unit="Row"
                ):
                    # Changing name of few Countries for convienience
                    if row["Region"] == "Brunei Darussalam":
                        row["Region"] = "Brunei"

                    if row["Region"] == "Lao People's Democratic Republic":
                        row["Region"] = "Laos"

                    if row["Region"] == "Viet Nam":
                        row["Region"] = "Vietnam"

                    if row["Region"] == "Russian Federation":
                        row["Region"] = "Russia"

                    # Populating Tables

                    # Populating main table
                    p = Population(
                        region=row["Region"],
                        country_code=int(row['Country Code']),
                        year=int(row["Year"]),
                        population=float(row["Population"])
                    )
                    p.save()

                    # Populating Asean Countries table
                    if p.region in ASEAN:
                        a.countries.add(p)
                    # if row["Region"] in ASEAN:
                    #     a.countries.add(p)

                    # Populating Saarc Countries table
                    if p.region in SAARC:
                        s.countries.add(p)

                    # Populating Brics_countries Countries table
                    if p.region in BRICS:
                        b.countries.add(p)

                    # Populating G4_countries Countries table
                    if p.region in G_four:
                        g_four.countries.add(p)

                    # Populating G5_countries Countries table
                    if p.region in G_five:
                        g_five.countries.add(p)

        except FileNotFoundError:
            print("File name is incorrect....Try Agian")
