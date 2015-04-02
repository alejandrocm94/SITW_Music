from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date



class Song(models.Model):
    name = models.TextField()
    duration = models.IntegerField()

    def __unicode__(self):
        return u"%s" % self.name

class Release(models.Model):
    name = models.TextField()
    date = models.DateField(default=date.today)
    kind = models.TextField()
    genre = models.TextField()
    song = models.ForeignKey(Song, default=1)

    def __unicode__(self):
        return u"%s" % self.name



class Artist(models.Model):
    name = models.TextField()
    area = models.TextField()
    release = models.ForeignKey(Release, default=1)
    biography = models.TextField(default="")
    score = models.DecimalField('Average score', max_digits=2, decimal_places=2, blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.name


class Playlist(models.Model):
    name = models.TextField()
    date = models.DateField(default = date.today)
    user = models.ForeignKey(User, default = 1, editable = False)
    songs = models.ManyToManyField(Song)

    def __unicode__(self):
        return u"%s" % self.name
    def get_absolute_url(self):
        return reverse('myplaylists:playlist_detail', kwargs={'pk': self.pk})
