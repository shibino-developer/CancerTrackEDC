# This serializer converts TestResult instances to and from JSON format.
from rest_framework import serializers
from .models import TestResult
# It specifies the TestResult model and includes all fields for serialization.
class TestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResult
        fields = '__all__'
