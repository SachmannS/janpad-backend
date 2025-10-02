from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password

from .models import Profile, ProfileOccupation, Review, Preference
from .serializers import (
    UserSerializer,
    ProfileSerializer,
    ProfileOccupationSerializer,
    ReviewSerializer,
    PreferenceSerializer,
    ProfileCardSimpleSerializer
)


# -------------------- Model ViewSets --------------------

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileOccupationViewSet(viewsets.ModelViewSet):
    queryset = ProfileOccupation.objects.all()
    serializer_class = ProfileOccupationSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class PreferenceViewSet(viewsets.ModelViewSet):
    queryset = Preference.objects.all()
    serializer_class = PreferenceSerializer


# -------------------- Auth Views --------------------

class RegisterView(APIView):
    def post(self, request):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already taken"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create(
            username=username,
            email=email,
            password=make_password(password)
        )
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({"message": "Login successful", "user": UserSerializer(user).data})
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Logged out successfully"})
    


class ProfileCardSimpleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileCardSimpleSerializer

    def get_queryset(self):
        queryset = Profile.objects.all().select_related("user", "city")

        city = self.request.query_params.get("city")
        occupation = self.request.query_params.get("occupation")
        speciality = self.request.query_params.get("speciality")
        username = self.request.query_params.get("username")

        if city:
            queryset = queryset.filter(city__name__iexact=city)

        if occupation:
            queryset = queryset.filter(profileoccupation__occupation__name__iexact=occupation)

        if speciality:
            queryset = queryset.filter(profileoccupation__speciality__name__iexact=speciality)

        if username:
            queryset = queryset.filter(user__username__iexact=username)

        return queryset.distinct()

        