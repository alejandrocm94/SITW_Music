from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import SlugRelatedField
from myplaylists.models import Song, Artist, Release, Playlist


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class SongSerializer(serializers.HyperlinkedModelSerializer):

    release = SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Song
        fields = ('name', 'duration', 'release')


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ('name', 'area', 'biography', 'score')


class ReleaseSerializer(serializers.HyperlinkedModelSerializer):

    artist = SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Release
        fields = ('name', 'year', 'kind', 'artist')


class PlaylistSerializer(serializers.HyperlinkedModelSerializer):

    songs = SlugRelatedField(
        many=True,
        queryset=Song.objects.all(),
        slug_field='name'
     )

    user = SlugRelatedField(
        read_only=True,
        slug_field='username'
     )


    class Meta:
        model = Playlist
        fields = ('name', 'user' ,'songs')