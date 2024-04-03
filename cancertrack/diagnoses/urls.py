from django.urls import path, include
from rest_framework import routers
from .views import DiagnosisViewSet

router = routers.DefaultRouter()
router.register(r'diagnoses', DiagnosisViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
