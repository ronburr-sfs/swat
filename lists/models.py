from django.db import models


class ListStatus(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class List(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True, default='')
    status = models.ForeignKey(ListStatus, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
