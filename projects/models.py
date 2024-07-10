from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):  # Class names should be CamelCase
    name = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(User, related_name='owned_projects', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='projects')

    def __str__(self):
        return self.name

class Task(models.Model):  # Class names should be CamelCase
    name = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    status = models.CharField(max_length=300, choices=[("todo", "TO DO"), ("inprogress", "IN PROGRESS"), ("done", "DONE")])
    due_date = models.DateField()

    def __str__(self):
        return self.name
