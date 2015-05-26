from django.contrib import admin
import models

# Register your models here.

admin.site.register(models.Artist)
admin.site.register(models.Release)
admin.site.register(models.Song)
admin.site.register(models.Playlist)
admin.site.register(models.UserProfile)