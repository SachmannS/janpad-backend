from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet,
    ProfileViewSet,
    ProfileOccupationViewSet,
    ReviewViewSet,
    PreferenceViewSet,
    RegisterView,
    LoginView,
    LogoutView,
    ProfileCardSimpleViewSet
)
from django.urls import path

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'profile-occupations', ProfileOccupationViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'preferences', PreferenceViewSet)
router.register(r'occupation/profile', ProfileCardSimpleViewSet, basename="profiles-card")

urlpatterns = router.urls + [
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
]