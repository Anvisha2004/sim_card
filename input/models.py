from django.db import models
from django.utils import timezone

class user(models.Model):
    first_name = models.CharField(max_length=100, default='firstname')
    last_name = models.CharField(max_length=100, default='lastname')
    sim_number = models.CharField(max_length=20, unique=True)
    phone_number = models.IntegerField(default=0)  # Adjust the default as needed
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='inactive')
    activation_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname} - {self.sim_number}"  # More descriptive representation

