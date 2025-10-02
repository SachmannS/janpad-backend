from rest_framework import serializers
from .models import Occupation, Speciality


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = "__all__"


class OccupationSerializer(serializers.ModelSerializer):
    specialities = SpecialitySerializer(many=True, read_only=True, source="speciality_set")

    class Meta:
        model = Occupation
        fields = ["id", "name", "specialities", "picture_url"]
