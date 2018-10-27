from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    """Задание"""
    text=models.CharField(max_length=200)
    time = models.TimeField()
    due_date = models.DateField()
    owner = models.ForeignKey(User)
    is_complete = models.BooleanField(default=False)
    category = models.CharField(max_length=200)

    def __str__(self):
        """Возвращает строковое представление модели"""
        return self.text

