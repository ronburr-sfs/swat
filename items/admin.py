from django.contrib import admin

from .models import ItemStatus
from .models import Item

admin.site.register(ItemStatus)
admin.site.register(Item)
