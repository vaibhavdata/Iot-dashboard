from django.contrib import admin
from . models import Device,Device_Type,All_Type,Service,Service_type
# Register your models here.
admin.site.register(Device)
admin.site.register(Device_Type)
admin.site.register(All_Type)
admin.site.register(Service)
admin.site.register(Service_type)
