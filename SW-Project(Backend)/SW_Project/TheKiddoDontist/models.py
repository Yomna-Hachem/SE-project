from django.db import models
from django.contrib.auth.models import User


class Appointment(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    dentist = models.CharField(max_length=100)
    timeslot = models.CharField(max_length=100)

    def returnstring(self):
        return f"{self.first_name} {self.last_name}"

class Review(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.PositiveIntegerField()

    def __str__(self):
        return f"Review by {self.patient.username}"

class UserInterfaceMixin:
    def get_full_name(self):
        pass

    def get_role(self):
        pass

class Doctor(models.Model, UserInterfaceMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    

    def get_full_name(self):
        return f"Dr. {self.first_name} {self.last_name}"

    def get_role(self):
        return "doctor"
    
class Patient(models.Model, UserInterfaceMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_role(self):
        return "patient"
