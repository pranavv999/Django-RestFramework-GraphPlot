from django.contrib import admin
from .models import (Population, Groupings)
from django_admin_listfilter_dropdown.filters import DropdownFilter

# Register your models here.


@admin.register(Population)
class PopulationAdmin(admin.ModelAdmin):
    list_display = ("region", "country_code", "year", "population")
    list_filter = [
        ("region", DropdownFilter),
        ("year", DropdownFilter),
        ("country_code", DropdownFilter),
        ("population", DropdownFilter)
    ]
    search_fields = ("region__startswith", "country_code__startswith")


@admin.register(Groupings)
class GroupingsAdmin(admin.ModelAdmin):
    list_display = ("group", "country_names")

    def country_names(self, obj):
        c = [str(c.region) for c in obj.countries.all()]
        c = list(set(c))
        return c
