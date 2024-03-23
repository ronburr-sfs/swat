from django.db import models

from projects.models import Project


class TaskPriority(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class TaskStatus(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True, default='')
    file = models.FileField(upload_to='tasks/', null=True, blank=True)
    priority = models.ForeignKey(TaskPriority, on_delete=models.CASCADE)
    status = models.ForeignKey(TaskStatus, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project.title + ' : ' + self.title
