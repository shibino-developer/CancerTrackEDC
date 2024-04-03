# This sets up the URLs for the test results API endpoints.
# It uses a router to automatically generate URL patterns for CRUD operations on test results.
# Requests to /test-results/ will be handled by the TestResultViewSet.
from django.urls import path, include
from rest_framework import routers
from .views import TestResultViewSet

router = routers.DefaultRouter()
router.register(r'test-results', TestResultViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
