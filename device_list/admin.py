from django.contrib import admin

# Register your models here.

from device_list.models import Device




class deviceAdmin(admin.ModelAdmin):
    fields = ['name', 'device_range']
    list_display = ('name', 'device_range')
    list_filter = ['name', 'device_range']
    search_fields = ['name', 'device_range']

admin.site.register(Device,deviceAdmin)


