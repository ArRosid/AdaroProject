from django.contrib import admin
from app.models import MachineIncident


@admin.register(MachineIncident)
class MachineIncidentAdmin(admin.ModelAdmin):
    list_display = ["machine", "description", "created_at", "start_time", "end_time", "duration", "shutdown_type", "shutdown_area"]
    search_fields = ["description", "machine"]
