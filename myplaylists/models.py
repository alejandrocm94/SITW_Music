from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Artist(models.Model):
    name = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    biography = models.TextField(default="")
    score = models.DecimalField('Average score', max_digits=2, decimal_places=2, blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.name


class Release(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    kind = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, default=1)

    def __unicode__(self):
        return u"%s" % self.name


class Song(models.Model):
    name = models.CharField(max_length=50)
    duration = models.CharField(max_length=10)
    release = models.ForeignKey(Release)

    def __unicode__(self):
        return u"%s" % self.name


class Playlist(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, default=1, editable=False)
    songs = models.ManyToManyField(Song)

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('myplaylists:playlist_detail', kwargs={'pk': self.pk})


class UserProfile(models.Model):
    user = models.ForeignKey(User, default=1, editable=False)
    image = models.ImageField(upload_to="myplaylists", blank=True, null=True)
    country = models.CharField(max_length=50, blank=True)
    description = models.TextField(default="", blank=True)

    def __unicode__(self):
        return u"%s" % self.user.username
    def get_absolute_url(self):
        return reverse('myplaylists:userprofile_detail', kwargs={'pk': self.pk})
