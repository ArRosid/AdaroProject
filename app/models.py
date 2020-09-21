from django.db import models
from app.choices import MachineIncidentChoices


class MachineIncident(models.Model):
    machine = models.CharField(max_length=100, choices=MachineIncidentChoices.machine_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    shutdown_type = models.CharField(max_length=100, choices=MachineIncidentChoices.shutdown_type)
    shutdown_area = models.CharField(max_length=100, choices=MachineIncidentChoices.shutdown_area)
    description = models.TextField()

    def __str__(self):
        return self.shutdown_type

    def duration(self):
        if not self.end_time:
            return "Unfinished"
        else:
            return str(self.end_time - self.start_time)

    def duration_minute(self):
        if not self.end_time:
            return 0
        else:
            return (self.end_time - self.start_time).total_seconds() / 60