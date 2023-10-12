from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.toDoList)
admin.site.register(models.Message)