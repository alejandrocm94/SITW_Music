from django.contrib.auth.models import User
from rest_framework import serializers
from myplaylists.models import Song, Artist, Release, Playlist


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ('name', 'duration')


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ('name', 'area', 'biography', 'score')


class ReleaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Release
        fields = ('name', 'year', 'kind')


class PlaylistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Playlist
        fields = ('name')