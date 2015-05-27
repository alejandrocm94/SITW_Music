from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.relations import HyperlinkedIdentityField, HyperlinkedRelatedField
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
    artist = HyperlinkedRelatedField(view_name='myplaylists:artist-detail', read_only=True)

    class Meta:
        model = Release
        fields = ('release_url', 'name', 'year', 'kind', 'artist')


class SongSerializer(serializers.HyperlinkedModelSerializer):

    song_url = HyperlinkedIdentityField(view_name='myplaylists:song-detail')
    release = HyperlinkedRelatedField(view_name='myplaylists:release-detail', read_only=True)

    class Meta:
        model = Song
        fields = ('song_url', 'name', 'duration', 'release')


class PlaylistSerializer(serializers.HyperlinkedModelSerializer):

    songs = HyperlinkedRelatedField(view_name='myplaylists:song-detail', read_only=True, many=True)
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Playlist
        fields = ('name', 'user', 'songs')