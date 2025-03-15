from django.db import models
from django.contrib.auth.models import User

class HeartRate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="heartrates")
    systolic = models.PositiveSmallIntegerField()
    diastolic = models.PositiveSmallIntegerField()
    pulse = models.PositiveSmallIntegerField()
    measured_in = models.DateTimeField()

    class Meta:
        ordering = ['-measured_in', ]

    def __str__(self):
        return f"{self.user} systolic is {self.systolic}, diastolic is {self.diastolic}, pulse is {self.pulse}"

    def to_dict(self):
        return {
            'user': self.user,
            'systolic': self.systolic,
            'diastolic': self.diastolic,
            'pulse': self.pulse,
            'date': self.measured_in
        }

    @property
    def get_pulse(self):
        return self.pulse

    @property
    def get_heartrate(self):
        return (self.systolic, self.diastolic)
