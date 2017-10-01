from rest_framework import serializers
from core.serializers import UserLiteSerializer
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    assigned_to = UserLiteSerializer(read_only=True)
    
    class Meta:
        model = Task
        fields = ['title', 'task', 'created_on', 'deadline', 'assigned_to']
