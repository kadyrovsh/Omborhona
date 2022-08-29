from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *

admin.site.register(Ombor)
admin.site.register(Client)
admin.site.register(Mahsulot)
admin.site.register(Stats)


