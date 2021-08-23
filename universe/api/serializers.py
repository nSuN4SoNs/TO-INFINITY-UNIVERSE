from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from universe.models import (
    Galaxy,
    StarSystem,
    Star,
    Planet,
    Moon
)


class GalaxySerializer(ModelSerializer):

    class Meta:
        model = Galaxy
        fields = "__all__"

class StarSystemSerializer(ModelSerializer):

    class Meta:
        model = StarSystem
        fields = "__all__"


class StarSerializer(ModelSerializer):

    class Meta:
        model = Star
        fields = "__all__"


class PlanetSerializer(ModelSerializer):

    class Meta:
        model = Planet
        fields = "__all__"

class MoonSerializer(ModelSerializer):

    class Meta:
        model = Moon
        fields = "__all__"

