from django import forms

from lists.models import List


class ListCreateForm(forms.ModelForm):
    class Meta:
        model= List
        fields= ["title", "body", "status"]


class ListEditForm(forms.ModelForm):
    class Meta:
        model= List
        fields= ["title", "body", "status"]
