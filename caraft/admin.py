from django.contrib import admin
from .models import *
# Register your models here.

class CaraftAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']
    
    
admin.site.register(Caraft,CaraftAdmin)
