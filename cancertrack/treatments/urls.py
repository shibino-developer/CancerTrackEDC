from django.urls import path, include
from rest_framework import routers
from .views import TreatmentViewSet

router = routers.DefaultRouter()
router.register(r'treatments', TreatmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
