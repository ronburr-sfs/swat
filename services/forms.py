from django import forms

from services.models import Service


class ServiceCreateForm(forms.ModelForm):
    class Meta:
        model= Service
        fields= ["title", "body", "status"]


class ServiceEditForm(forms.ModelForm):
    class Meta:
        model= Service
        fields= ["title", "body", "status"]
