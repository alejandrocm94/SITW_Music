from django.forms import ModelForm
from myplaylists.models import Artist, Release, Song, Playlist, UserProfile, Review


class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = "__all__"


class ReleaseForm(ModelForm):
    class Meta:
        model = Release
        fields = "__all__"


class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = "__all__"


class PlaylistForm(ModelForm):
    class Meta:
        model = Playlist
        fields = "__all__"


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('name', 'surname', 'image', 'location', 'description')