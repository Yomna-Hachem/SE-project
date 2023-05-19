from django.db import models


class Appointment(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    dentist = models.CharField(max_length=100)
    timeslot = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
