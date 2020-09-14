from django.contrib import admin
from app.models import MachineIncident


@admin.register(MachineIncident)
class MachineIncidentAdmin(admin.ModelAdmin):
    list_display = ["description", "created_at", "start_time", "end_date", "duration", "shutdown_type", "shutdown_area"]
    search_fields = ["description"]
