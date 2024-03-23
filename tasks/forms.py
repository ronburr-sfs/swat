from django import forms

from tasks.models import Task


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model= Task
        fields= ["project", "title", "body", "file", "priority", "status"]


class TaskEditForm(forms.ModelForm):
    class Meta:
        model= Task
        fields= ["project", "title", "body", "file", "priority", "status"]
