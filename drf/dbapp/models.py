from django.db import models


# Create your models here.
# Main Table
class Population(models.Model):
    region = models.CharField(max_length=200)
    country_code = models.IntegerField()
    year = models.IntegerField()
    population = models.FloatField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.region} - {self.year}"


# Country group table
class Groupings(models.Model):
    group = models.CharField(max_length=200)
    countries = models.ManyToManyField(Population, related_name='groups')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.group}"
