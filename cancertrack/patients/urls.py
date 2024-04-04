# Defines URL patterns for the patient-related endpoints in your 
# DRF API

# Imports the path function and include function from Django's URL patterns module.

from django.urls import path, include
#  Imports the routers module from Django REST framework, 
# provides a simple way to create URL patterns for viewsets.
from rest_framework import routers
# Imports the PatientViewSet viewset from the current package's views module.
from .views import PatientViewSet
# Creates a router instance using Django REST framework's DefaultRouter. 
# This router will generate URL patterns for the viewsets registered with it.
router = routers.DefaultRouter()
# Registers the PatientViewSet viewset with the router. 
# This associates the viewset with a URL pattern prefix patients/, 
# which will be used to access patient-related endpoints.
router.register(r'patients', PatientViewSet)
# Defines the list of URL patterns for the Django application.
urlpatterns = [
    #  Includes the URL patterns generated by the router in the root URL patterns of the application. 
    # This means that any URL pattern generated by the router will be prefixed with the root URL. 
    # For example, patients/ will be accessible at the root URL.
    # path('patients/', PatientViewSet.as_view({'get': 'list'}), name='patient-list'),
    path('', include(router.urls)),
     # Add URL patterns for OAuth authorization and callback
     
    # path('authorize/', PatientViewSet.as_view({'get': 'authorize'}), name='oauth_authorize'),
    # path('oauth2callback/', PatientViewSet.as_view({'get': 'oauth2callback'}), name='oauth_callback'),

]
