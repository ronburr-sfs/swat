from django.db import models

from lists.models import List


class ItemStatus(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Item(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True, default='')
    status = models.ForeignKey(ItemStatus, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
