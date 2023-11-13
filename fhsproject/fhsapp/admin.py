from django.contrib import admin

# Register your models here.
from .models import Registration,Order
admin.site.register(Registration)
admin.site.register(Order)