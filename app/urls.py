from django.urls import path
from app.views import (
    MachineIncidentList,
    MachineIncidentCreate,
    MachineIncidentUpdate,
    MachineIncidentDelete,
    report
)


urlpatterns = [
    path("", MachineIncidentList.as_view(), name="MachineIncidentList"),
    path("create/", MachineIncidentCreate.as_view(), name="MachineIncidentCreate"),
    path("update/<int:pk>/", MachineIncidentUpdate.as_view(), name="MachineIncidentUpdate"),
    path("delete/<int:pk>/", MachineIncidentDelete.as_view(), name="MachineIncidentDelete"),
    path("report/", report, name="report"),
]