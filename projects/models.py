from django.db import models


class ProjectCategory(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class ProjectPriority(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class ProjectStatus(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Project(models.Model):
    category = models.ForeignKey(
        ProjectCategory, on_delete=models.CASCADE, default=1)
    priority = models.ForeignKey(
        ProjectPriority, on_delete=models.CASCADE, default=3)
    status = models.ForeignKey(
        ProjectStatus, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True, default='')

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
