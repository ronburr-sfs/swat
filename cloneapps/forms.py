from django import forms

from cloneapps.models import Cloneapp


class CloneappCreateForm(forms.ModelForm):
    class Meta:
        model= Cloneapp
        fields= ["title", "body", "status"]


class CloneappEditForm(forms.ModelForm):
    class Meta:
        model= Cloneapp
        fields= ["title", "body", "status"]
