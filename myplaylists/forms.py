from django.forms import ModelForm
from myplaylists.models import Artist, Release, Song, Playlist

class ArtistForm(ModelForm):
    class Meta:
        model = Artist

class ReleaseForm(ModelForm):
    class Meta:
        model = Release

class SongForm(ModelForm):
    class Meta:
        model = Song

class PlaylistForm(ModelForm):
    class Meta:
        model = Playlist