from django.contrib import admin
from music import models

# Register your models here.
admin.site.register(models.Album)
admin.site.register(models.Song)
