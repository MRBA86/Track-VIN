from django.contrib import admin
from .models import Car , CarType , EmergencySpec , OptionalSpec


admin.site.register(Car)

admin.site.register(CarType)

admin.site.register(OptionalSpec)


admin.site.register(EmergencySpec)



# Register your models here.
