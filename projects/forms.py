from django.forms import ModelForm, Select, Textarea

from projects.models import Project


class ProjectCreateForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectEditForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
