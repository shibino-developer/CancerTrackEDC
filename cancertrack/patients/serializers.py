# Defines a serializer class PatientSerializer using Django Rest Framework's ModelSerializer.
# Imports the serializers module from DRF.
# Provides tools for serializing and deserializing data.
from rest_framework import serializers
#  Imports the Patient model from the current package.
from .models import Patient
# Defines a serializer class named PatientSerializer that inherits from serializers.ModelSerializer

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        # This inner class within the serializer contains metadata options for the serialization process.
        model = Patient 
        # Specifies the model to be serialized, which is Patient in this case.
        fields = '__all__'
        # Indicates that all fields of the Patient model should be included in the serialization.
