from rest_framework import serializers
from .models import Project, Task
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ProjectSerializer(serializers.ModelSerializer):  # Fixed typo: ProjectSerialzer to ProjectSerializer
    owner = UserSerializer(read_only=True)
    members = UserSerializer(many=True, read_only=True)  # Fixed typo: memeber to members

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'owner', 'members']

class TaskSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'project', 'assigned_to', 'status', 'due_date']
