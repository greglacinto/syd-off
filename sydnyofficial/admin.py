from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Audio)
admin.site.register(models.Video)
admin.site.register(models.Image)