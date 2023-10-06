from django import forms
from .models import toDoList

class toDoListForm(forms.ModelForm):
    class Meta:
        model = toDoList
        fields = ['userId','taskName', 'progress', 'dueDate']


class MessageForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)