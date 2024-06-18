from django.db import models
from django.contrib.auth.models import User

class EmergencySpec(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class OptionalSpec(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CarType(models.Model):
    name = models.CharField(max_length=50)
    certificate_number = models.CharField(max_length=50)
    commercial_name = models.CharField(max_length=50)
    ilk = models.CharField(max_length=20)
    net_power_engine = models.IntegerField()
    torque = models.IntegerField()
    max_speed = models.IntegerField()
    fuel_consumption = models.FloatField()
    energy_level = models.CharField(max_length=1)
    pollution_level = models.CharField(max_length=10)
    noise_level = models.FloatField()
    guarantee_period = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.certificate_number}"



class Car(models.Model):
    
    engine_number = models.CharField(max_length=17, null=True, blank=True)
    vin_number = models.CharField(max_length=17, unique=True , null=True, blank=True)
    car_type = models.ForeignKey(CarType, on_delete=models.SET_NULL , null=True, blank=True )
    owner = models.ForeignKey(User, on_delete= models.SET_NULL , null=True, blank=True)
    emergency_spec = models.ManyToManyField(EmergencySpec )
    optional_facilities = models.ManyToManyField(OptionalSpec)
    accepted_date = models.DateField(null=True, blank=True)
    created_date = models.DateField(null=True, blank=True)
    delivery_date = models.DateField(null=True, blank=True)
    
    def __str__(self) :
        return f'{self.vin_number}- {self.owner}'



# Create your models here.
