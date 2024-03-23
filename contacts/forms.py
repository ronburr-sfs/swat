from django import forms

from contacts.models import Contact


class ContactCreateForm(forms.ModelForm):
    class Meta:
        model= Contact
        fields= ["title", "body", "status"]


class ContactEditForm(forms.ModelForm):
    class Meta:
        model= Contact
        fields= ["title", "body", "status"]
