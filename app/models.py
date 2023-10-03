from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django import forms


class toDoList(models.Model):
    id=models.AutoField(primary_key=True)
    taskName=models.CharField(max_length=100,null=True)
    progress=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)],null=True)
    dueDate=models.DateTimeField(null=True)
