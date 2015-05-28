from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.fields import ModelField
from rest_framework.relations import HyperlinkedIdentityField, HyperlinkedRelatedField, StringRelatedField
from rest_framework.serializers import SlugRelatedField
from myplaylists.models import Song, Artist, Release, Playlist


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ('name', 'area', 'biography')


class ReleaseSerializer(serializers.HyperlinkedModelSerializer):

    release_url = HyperlinkedIdentityField(view_name='myplaylists:release-detail')
    artist = StringRelatedField()

    class Meta:
        model = Release
        fields = ('release_url', 'name', 'year', 'kind', 'artist')


class SongSerializer(serializers.HyperlinkedModelSerializer):

    song_url = HyperlinkedIdentityField(view_name='myplaylists:song-detail')
    release = StringRelatedField()

    class Meta:
        model = Song
        fields = ('song_url', 'name', 'duration', 'release')


class PlaylistSerializer(serializers.HyperlinkedModelSerializer):

    playlist_url = HyperlinkedIdentityField(view_name='myplaylists:playlist-detail')
    songs = StringRelatedField(many=True)
    user = StringRelatedField()

    class Meta:
        model = Playlist
        fields = ('playlist_url', 'name', 'user', 'songs')