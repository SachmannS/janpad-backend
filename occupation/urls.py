from rest_framework.routers import DefaultRouter
from .views import OccupationViewSet, SpecialityViewSet

router = DefaultRouter()
router.register(r'occupations', OccupationViewSet)
router.register(r'specialities', SpecialityViewSet)

urlpatterns = router.urls
