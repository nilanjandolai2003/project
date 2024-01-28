from django.contrib import admin
from .models import student,Role,department
# Register your models here.
admin.site.register(student)
admin.site.register(Role)
admin.site.register(department)