from django.db import models 

# Imports the models module from Django, which provides tools for defining database models

class Patient(models.Model): 
# Defines a new class named Patient, which represents a database model. 
# It inherits from models.Model, indicating that Patient is a Django model.
    name = models.CharField(max_length=100)  
    # defines a field named name for the Patient model with maximum length of 100 characters.
    age = models.IntegerField()
    # defines an age field for the Patient model which stores integer values.
    # Add more fields as needed
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()