from django import forms

from items.models import Item


class ItemCreateForm(forms.ModelForm):
    class Meta:
        model= Item
        fields= ["list", "title", "body", "status"]


class ItemEditForm(forms.ModelForm):
    class Meta:
        model= Item
        fields= ["list", "title", "body", "status"]
