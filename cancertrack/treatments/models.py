from django.db import models
from patients.models import Patient

class Treatment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    treatment_type = models.CharField(max_length=100)
    duration = models.DurationField()
    # Add more fields as needed
