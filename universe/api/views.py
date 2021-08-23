from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from universe.models import (
    Galaxy,
    StarSystem,
    Star,
    Planet,
    Moon
)
from universe.api.serializers import (
    GalaxySerializer,
    StarSystemSerializer,
    StarSerializer,
    PlanetSerializer,
    MoonSerializer
)

class GalaxyViewSet(ModelViewSet):

    queryset = Galaxy.objects.all()
    serializer_class = GalaxySerializer

class StarSystemViewSet(ModelViewSet):

    queryset = StarSystem.objects.all()
    serializer_class = StarSystemSerializer

class StarViewSet(ModelViewSet):

    queryset = Star.objects.all()
    serializer_class = StarSerializer

class PlanetViewSet(ModelViewSet):

    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer

class MoonViewSet(ModelViewSet):

    queryset = Moon.objects.all()
    serializer_class = MoonSerializer
