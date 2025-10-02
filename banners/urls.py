from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import EventsViewSet, AdvertisementViewSet

router = DefaultRouter()

router.register('events', EventsViewSet, basename="events")
router.register('adds', AdvertisementViewSet, basename="adds")

urlpatterns = [

] + router.urls