from django.contrib import admin

from .models import ProjectCategory
from .models import ProjectPriority
from .models import ProjectStatus
from .models import Project

admin.site.register(ProjectCategory)
admin.site.register(ProjectPriority)
admin.site.register(ProjectStatus)
admin.site.register(Project)
