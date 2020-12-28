from rest_framework import serializers


class PopulationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    region = serializers.CharField()
    country_code = serializers.IntegerField()
    year = serializers.IntegerField()
    population = serializers.FloatField()


class ProblemOneSerializer(serializers.Serializer):
    region = serializers.CharField()
    year = serializers.IntegerField()
    population = serializers.FloatField()


class ProblemThreeSerializer(serializers.Serializer):
    year = serializers.IntegerField()
    total_population = serializers.IntegerField()
