from rest_framework import viewsets
from .models import State, City
from .serializers import StateSerializer, CitySerializer

# Create your views here.
class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
