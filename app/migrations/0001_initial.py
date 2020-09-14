# Generated by Django 3.0 on 2020-09-14 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MachineIncident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('start_time', models.DateTimeField()),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('shutdown_type', models.CharField(choices=[('fully_shutdown', 'Fully Shutdown'), ('running_with_fail', 'Running with Fail')], max_length=100)),
                ('shutdown_area', models.CharField(choices=[('genset_power', 'Genset/Power'), ('mcc', 'MCC'), ('feeder', 'Feeder'), ('breaker', 'Breaker'), ('cv910', 'CV910'), ('sizer', 'Sizer'), ('cv911', 'CV911'), ('scada_plc', 'SCADA & PLC'), ('sampler_system', 'Sampler System'), ('iron_trap', 'Iron Trap'), ('metal_detector', 'Metal Detector'), ('belt_scale', 'Belt Scale')], max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
