from django.contrib import admin
from main.models import *


# Register your models here.


class PodpischikiAdmin(admin.ModelAdmin):
    pass


admin.site.register(Podpischiki, PodpischikiAdmin)
