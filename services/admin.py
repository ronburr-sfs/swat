from django.contrib import admin

from .models import ServiceStatus
from .models import Service

admin.site.register(ServiceStatus)
admin.site.register(Service)
