from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Event)
admin.site.register(Tags)
admin.site.register(EventComment)
admin.site.register(Email)
