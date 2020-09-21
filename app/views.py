from django.shortcuts import render
from django.views import generic
from app.models import MachineIncident
from django.urls import reverse_lazy
from app.forms import MachineIncidentForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils import timezone
import datetime
import pandas as pd
from calendar import monthrange
from app.choices import MachineIncidentChoices

@method_decorator(login_required, name="dispatch")
class MachineIncidentList(generic.ListView):
    model = MachineIncident
    template_name = "app/machine_incident_list.html"
    context_object_name = "incidents"


@method_decorator(login_required, name="dispatch")
class MachineIncidentCreate(generic.CreateView):
    model = MachineIncident
    template_name = "app/machine_incident_create.html"
    success_url = reverse_lazy("MachineIncidentList")
    form_class = MachineIncidentForm


@method_decorator(login_required, name="dispatch")
class MachineIncidentUpdate(generic.UpdateView):
    model = MachineIncident
    template_name = "app/machine_incident_create.html"
    context_object_name = "incident"
    form_class = MachineIncidentForm
    success_url = reverse_lazy("MachineIncidentList")


@method_decorator(login_required, name="dispatch")
class MachineIncidentDelete(generic.DeleteView):
    model = MachineIncident
    template_name = "app/machine_incident_delete.html"
    success_url = reverse_lazy("MachineIncidentList")


def report(request):
    data = []
    start_date = datetime.date(2020, 8, 1)
    end_date = datetime.datetime.now().date()
    month_list = [i.strftime("%b-%y") for i in pd.date_range(start=start_date, end=end_date, freq='MS')]
    for month in month_list:
        date = datetime.datetime.strptime(month, "%b-%y")
        total_time = monthrange(date.year, date.month)[1] * 24 * 60
        for machine in MachineIncidentChoices.machine_choices:
            down_time = 0
            incidents = MachineIncident.objects.filter(
                start_time__month=date.month,
                start_time__year=date.year,
                machine=machine[0]
            )
            for inc in incidents:
                down_time += inc.duration_minute()

            up_percent = (total_time - down_time) / total_time * 100
            down_percent = down_time / total_time * 100

            data.append({
                "month": month,
                "machine": machine[1],
                "up_percent": "%.3f" % up_percent,
                "down_percent": "%.3f" % down_percent
            })

    return render(request, "app/report.html", {"data": data})
