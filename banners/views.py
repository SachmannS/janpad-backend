from django.shortcuts import render
from rest_framework import viewsets
from .models import Advertisement, Events
from .serializers import AdvertisementSerializer, EventsSerializer

# Create your views here.
class EventsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EventsSerializer

    def get_queryset(self):
        queryset = Events.objects.all().select_related('orgainizer', 'orgainizer__city')
        city_id = self.request.query_params.get('city', None)
        print(city_id)
        if city_id:
            queryset = queryset.filter(orgainizer__city__name=city_id)
        return queryset

class AdvertisementViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AdvertisementSerializer

    def get_queryset(self):
        queryset = Advertisement.objects.all().select_related('author', 'city')
        city_id = self.request.query_params.get('city', None)
        if city_id:
            queryset = queryset.filter(city__name=city_id)
        return queryset
