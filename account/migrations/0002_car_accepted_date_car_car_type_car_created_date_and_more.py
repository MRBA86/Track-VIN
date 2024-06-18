# Generated by Django 5.0.6 on 2024-06-12 08:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='accepted_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='car_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.cartype'),
        ),
        migrations.AddField(
            model_name='car',
            name='created_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='delivery_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='emergency_spec',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.emergencyspec'),
        ),
        migrations.AddField(
            model_name='car',
            name='engine_number',
            field=models.CharField(blank=True, max_length=17, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='optional_facilities',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.optionalspec'),
        ),
        migrations.AddField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='car',
            name='vin_number',
            field=models.CharField(blank=True, max_length=17, null=True, unique=True),
        ),
    ]