from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *



# Register your models here.
admin.site.register(Evader_user)
admin.site.unregister(Group)
