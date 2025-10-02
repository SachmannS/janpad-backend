from rest_framework import viewsets, views
from .models import Occupation, Speciality
from .serializers import OccupationSerializer, SpecialitySerializer


class OccupationViewSet(viewsets.ModelViewSet):
    queryset = Occupation.objects.all()
    serializer_class = OccupationSerializer


class SpecialityViewSet(viewsets.ModelViewSet):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer

class FetchProfilesFromOccupation(views.APIView):
    def get(request):
        
        ...
