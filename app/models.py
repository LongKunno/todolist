from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django import forms
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone

class toDoList(models.Model):
    userId=models.IntegerField(null=True)
    taskName=models.CharField(max_length=100,null=True)
    progress=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)],null=True)
    dueDate=models.DateTimeField(null=True)

    def add_one_day_to_dueDate(self):
        self.dueDate += timedelta(days=1)
        self.save()

    def add_one_day_to_dueDate_out_of_date(self):
        self.dueDate = timezone.now() + timedelta(days=1)
        self.save()

    def minus_one_day_to_dueDate(self):
        self.dueDate -= timedelta(days=1)
        self.save()

    def __str__(self):
        return f'({self.dueDate} - userId:{self.userId}) {self.taskName}:{self.progress}'

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE,null=True)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE,null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'({self.timestamp}) {self.sender} to {self.receiver}: {self.content}'
    



