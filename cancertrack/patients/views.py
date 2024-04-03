# Defines a viewset class PatientViewSet using DRF's ModelViewSet.
# Imports the viewsets module from DRF,
#  which provides a set of tools for building API views.

from rest_framework import viewsets

#  Imports the Patient model from the current package.
from .models import Patient
#  Imports the PatientSerializer serializer from the current package.
from .serializers import PatientSerializer

# Defines a viewset class named PatientViewSet that inherits from viewsets.ModelViewSet. 
# ModelViewSet is a subclass of GenericViewSet 
# and provides default implementations for CRUD (Create, Retrieve, Update, Delete) operations on a model.
class PatientViewSet(viewsets.ModelViewSet):
# Specifies the queryset used to retrieve data from the database. 
    # In this case, it retrieves all Patient objects from the database.
    queryset = Patient.objects.all()
# Specifies the serializer class to use for serializing and deserializing data. 
# Here, PatientSerializer is used, which we defined earlier to serialize Patient objects.
    serializer_class = PatientSerializer
