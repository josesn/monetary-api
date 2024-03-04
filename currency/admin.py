from django.contrib import admin
from .models import ExchargeRate

class ExchargeRageAdmin(admin.ModelAdmin):
    model = ExchargeRate
    
admin.site.register(ExchargeRate, ExchargeRageAdmin)