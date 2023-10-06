from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django import forms
from django.contrib.auth.models import User

class toDoList(models.Model):
    id=models.AutoField(primary_key=True)
    userId=models.IntegerField(null=True)
    taskName=models.CharField(max_length=100,null=True)
    progress=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)],null=True)
    dueDate=models.DateTimeField(null=True)

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.sender} to {self.receiver}'

