from django.db import models
from django.contrib.auth.models import User

from projects.models import Project


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app = models.CharField(max_length=200, null=True)
    app_id = models.IntegerField(null=True)
    body = models.TextField(blank=True, default='')

    def __str__(self):
        return 'Comment ' + str(self.id)
