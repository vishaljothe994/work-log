from django.contrib import admin
from .models import Vehicle ,Car
# Register your models here.

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
 list_display=('reg_no', 'owner')

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
 list_display=('vehicle', 'car_model')

#admin.site.register(Student)

