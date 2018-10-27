from django import forms

from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text', 'due_date', 'time', 'category']
        labels = {'text': 'Task', 'due_date': 'Due date (In format: yyyy-mm-dd)', 'time': 'Time (In formate: hh:mm)'}
