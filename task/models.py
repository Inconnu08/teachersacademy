from django.db import models
from django.utils import timezone

from TeachersAcademy import settings


class Task(models.Model):
    title = models.CharField(max_length=100)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tasks', null=True)
    task = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField()

    def __str__(self):
        return f'Task: {self.title}'
