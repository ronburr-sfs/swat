from django import forms

from comments.models import Comment


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields= ["app", "app_id", "body"]


class CommentEditForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields= ["app", "app_id", "body"]
