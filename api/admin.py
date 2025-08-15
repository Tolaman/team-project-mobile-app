from django.contrib import admin
from .models import Report, Shelter
#from django.contrib.gis import admin as gis_admin

# Register your models here.
admin.site.register(Report)
admin.site.register(Shelter)