from django.contrib import admin
from . import models

admin.site.register(models.Song)
admin.site.register(models.Musician)
admin.site.register(models.Album)