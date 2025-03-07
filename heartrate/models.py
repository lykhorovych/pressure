from django.db import models
from django.contrib.auth.models import User

class HeartRate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="heartrates")
    systolic = models.PositiveSmallIntegerField()
    diastolic = models.PositiveSmallIntegerField()
    pulse = models.PositiveSmallIntegerField()
    measured_in = models.DateTimeField()
