# Defines a TestResult class with fields for the patient (using a foreign key to the Patient model), test name, 
# result, and date.

from django.db import models
from patients.models import Patient

class TestResult(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    test_type = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
    date = models.DateField()
    # Add more fields as needed
