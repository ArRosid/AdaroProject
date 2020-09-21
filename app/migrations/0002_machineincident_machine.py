# Generated by Django 3.0 on 2020-09-20 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='machineincident',
            name='machine',
            field=models.CharField(choices=[('machine1', 'Machine 1'), ('machine2', 'Machine 2')], default='machine1', max_length=100),
            preserve_default=False,
        ),
    ]