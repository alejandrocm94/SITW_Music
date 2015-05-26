from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date


class Artist(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="myplaylists/artistPics", blank=True, null=True)
    area = models.CharField(max_length=50)
    biography = models.TextField(default="")

    def __unicode__(self):
        return u"%s" % self.name


class Release(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="myplaylists/releasePics", blank=True, null=True)
    year = models.IntegerField()
    kind = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, default=1)

    def __unicode__(self):
        return u"%s" % self.name


class Song(models.Model):
    name = models.CharField(max_length=50)
    duration = models.CharField(max_length=10)
    release = models.ForeignKey(Release)

    @property
    def release__name(self):
        return self.release.name

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
    name = models.CharField(max_length=50, blank=True)
    surname = models.CharField(max_length=50, blank=True)
    user = models.ForeignKey(User, default=1, editable=False)
    image = models.ImageField(upload_to="myplaylists/profilePics", blank=True, null=True)
    location = models.CharField(max_length=50, blank=True)
    description = models.TextField(default="", blank=True)

    def __unicode__(self):
        return u"%s" % self.user.username

    def get_absolute_url(self):
        return reverse('myplaylists:userprofile_detail', kwargs={'pk': self.pk})


class Review(models.Model):
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)

    class Meta:
        abstract = True


class ReleaseReview(Review):
    release = models.ForeignKey(Release)
