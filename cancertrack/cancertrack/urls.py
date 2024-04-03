"""
URL configuration for cancertrack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Imports the admin module, which provides the Django admin interface.
from django.contrib import admin
#  Imports the path function and include function from Django's URL patterns module.
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), 
    # Defines a URL pattern for the patients app. When a URL starting with patients/ is requested, 
    # Django will include the URL patterns defined in the patients.urls module.

    path('patients/', include('patients.urls')),
    path('test-results/', include('test_results.urls')),
    path('diagnoses/', include('diagnoses.urls')),
    path('treatments/', include('treatments.urls')),
    
]
