from django.db import models
from patients.models import Patient

class Diagnosis(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnosis_code = models.CharField(max_length=100)
    description = models.TextField()
    # Add more fields as needed
