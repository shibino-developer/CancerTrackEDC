# This viewset provides CRUD functionality for TestResult instances.
# It specifies the queryset and serializer class to be used.

from rest_framework import viewsets
from .models import TestResult
from .serializers import TestResultSerializer

class TestResultViewSet(viewsets.ModelViewSet):
    queryset = TestResult.objects.all()
    serializer_class = TestResultSerializer
