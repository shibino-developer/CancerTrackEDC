from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)  # Providing a default value for age
    date_of_birth = models.DateField(default='1900-01-01')  # Providing a default date
    gender_choices = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    gender = models.CharField(max_length=10, choices=gender_choices, default='O')  # Providing a default gender
    address = models.CharField(max_length=100, default='Unknown')
    phone_number = models.CharField(max_length=15, default='')
    email = models.EmailField(default='')

    def __str__(self):
        return self.name
