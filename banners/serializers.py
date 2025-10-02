from rest_framework import serializers
from .models import Advertisement, Events, Profile
from account.serializers import ProfileCardSimpleSerializer  # reuse previous profile serializer

class AdvertisementSerializer(serializers.ModelSerializer):
    author = ProfileCardSimpleSerializer(read_only=True)

    class Meta:
        model = Advertisement
        fields = ['headline', 'description', 'author', 'city']

class EventsSerializer(serializers.ModelSerializer):
    organizer = ProfileCardSimpleSerializer(source="orgainizer", read_only=True)

    class Meta:
        model = Events
        fields = ['headline', 'description', 'organizer', 'date']
