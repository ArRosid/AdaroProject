from django.db import models
from app.choices import MachineIncidentChoices


# Create your models here.
class MachineIncident(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    shutdown_type = models.CharField(max_length=100, choices=MachineIncidentChoices.shutdown_type)
    shutdown_area = models.CharField(max_length=100, choices=MachineIncidentChoices.shutdown_area)
    description = models.TextField()

    def __str__(self):
        return self.shutdown_type

    def duration(self):
        if not self.end_date:
            return "Unfinished"
        else:
            return str(self.end_date - self.start_time)
