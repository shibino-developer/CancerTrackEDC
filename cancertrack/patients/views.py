# Defines a viewset class PatientViewSet using DRF's ModelViewSet.
# Imports the viewsets module from DRF,
#  which provides a set of tools for building API views.

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import redirect

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
     # Define an action to handle the OAuth authorization redirect
    @action(detail=False, methods=['GET'], url_path='authorize')
    def authorize(self, request):
        # Redirect to the OAuth authorization URL
        # Replace 'authorization_url' with your actual OAuth authorization URL
        authorization_url = 'https://accounts.google.com/o/oauth2/auth'  # Replace with your actual OAuth authorization URL
        return redirect(authorization_url)

    # Define an action to handle the OAuth callback
    @action(detail=False, methods=['GET'], url_path='oauth2callback')
    def oauth2callback(self, request):
        # Handle the OAuth callback logic here
        # This is where you exchange the authorization code for an access token
        # and then use the access token to authenticate the user
        # Once authenticated, you can redirect the user to the desired endpoint
        return Response({'message': 'OAuth callback handled successfully'})
