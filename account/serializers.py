from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, ProfileOccupation, Review, Preference, SocialMedia


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class ProfileOccupationSerializer(serializers.ModelSerializer):
    occupation_name = serializers.CharField(source="occupation.name", read_only=True)
    speciality_name = serializers.CharField(source="speciality.name", read_only=True)

    class Meta:
        model = ProfileOccupation
        fields = ["id", "occupation", "occupation_name", "speciality", "speciality_name"]


class ReviewSerializer(serializers.ModelSerializer):
    review_by = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ["id", "profile", "review_by", "rating", "review", "created"]


class PreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preference
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    profile_picture_url = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ["id", "user", "city", "description", "profile_picture_url"]

    def get_profile_picture_url(self, obj):
        request = self.context.get("request")
        if obj.profile_picture and hasattr(obj.profile_picture, 'url'):
            return request.build_absolute_uri(obj.profile_picture.url)
        return None



class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ["instagram", "x", "facebook", "threads", "linkedIn", "phone_number"]


class ProfileCardSimpleSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="user.username", read_only=True)
    rating = serializers.SerializerMethodField()
    social_media = serializers.SerializerMethodField()
    profile_picture = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ["name", "description", "rating", "social_media", "profile_picture"]

    def get_rating(self, obj):
        reviews = Review.objects.filter(profile=obj).values_list("rating", flat=True)
        if reviews:
            return round(sum(reviews) / len(reviews), 1)
        return None

    def get_social_media(self, obj):
        try:
            social = SocialMedia.objects.get(user=obj.user)
            return SocialMediaSerializer(social).data
        except SocialMedia.DoesNotExist:
            return {}
    
    def get_profile_picture(self, obj):
        request = self.context.get("request")  # needed to build full absolute URL
        if obj.profile_picture and hasattr(obj.profile_picture, "url"):
            return request.build_absolute_uri(obj.profile_picture.url) if request else obj.profile_picture.url
        return None