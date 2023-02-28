from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class EmployeeAdmin(UserAdmin):
    pass
admin.site.register(Employee, EmployeeAdmin)

UserAdmin.fieldsets += ('Custom fields set', {'fields': ('name','state')}),

admin.site.register(College)
admin.site.register(City)
admin.site.register(State)




# Register your models here.
