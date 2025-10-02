from rest_framework.routers import DefaultRouter
from .views import StateViewSet, CityViewSet

router = DefaultRouter()
router.register(r'states', StateViewSet)
router.register(r'cities', CityViewSet)

urlpatterns = router.urls
