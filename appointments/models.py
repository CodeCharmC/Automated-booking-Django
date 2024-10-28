from django.db import models

class Appointment(models.Model):
   patient_name = models.CharField(max_length=100)
   appointment_date = models.DateTimeField()
   doctor_name = models.CharField(max_length=100)
   status = models.CharField(max_length=10, choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Pending')
