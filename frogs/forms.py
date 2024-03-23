from django import forms

from frogs.models import Frog


class FrogCreateForm(forms.ModelForm):
    class Meta:
        model= Frog
        fields= ["title", "body", "status"]


class FrogEditForm(forms.ModelForm):
    class Meta:
        model= Frog
        fields= ["title", "body", "status"]
