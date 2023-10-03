from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator



class Form(forms.Form):
    taskName = forms.CharField(max_length=100)
    progress = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    dueDate = forms.DateTimeField()
    # def reset():
        
