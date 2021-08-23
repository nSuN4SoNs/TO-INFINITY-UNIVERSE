from django.urls import path, include
from rest_framework.routers import DefaultRouter
from universe.api.views import (
    GalaxyViewSet,
    StarSystemViewSet,
    StarViewSet,
    PlanetViewSet,
    MoonViewSet
)

router = DefaultRouter()

router.register("galaxies", GalaxyViewSet)
router.register("starsystems", StarSystemViewSet)
router.register("stars", StarViewSet)
router.register("planets", PlanetViewSet)
router.register("moons", MoonViewSet)

urlpatterns = [
    path("", include(router.urls))
]
