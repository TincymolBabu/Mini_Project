from django.contrib import admin

# Register your models here.
from .models import Employee
from .models import LeaveApplication,Employeelist

admin.site.register(Employee)
admin.site.register(LeaveApplication)
# admin.py
admin.site.register(Employeelist)