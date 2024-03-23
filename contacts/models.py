from django.db import models


class ContactStatus(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Contact(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True, default='')
    status = models.ForeignKey(ContactStatus, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
