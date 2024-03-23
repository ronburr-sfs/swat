from django.contrib import admin

from .models import TaskPriority
from .models import TaskStatus
from .models import Task

admin.site.register(TaskPriority)
admin.site.register(TaskStatus)
admin.site.register(Task)
