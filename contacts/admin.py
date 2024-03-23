from django.contrib import admin

from .models import ContactStatus
from .models import Contact

admin.site.register(ContactStatus)
admin.site.register(Contact)
