from django import forms
from app.models import MachineIncident


class MachineIncidentForm(forms.ModelForm):
    class Meta:
        model = MachineIncident
        fields = ["machine", "start_time", "end_time", "shutdown_type", "shutdown_area", "description"]
