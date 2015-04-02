from django.shortcuts import render

# Create your views here.
# Create your views here.

from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.views.generic.edit import CreateView

from models import Artist, Release, Song, Playlist
from forms import ArtistForm, ReleaseForm, SongForm, PlaylistForm

class PlaylistDetail(DetailView):
    model = Playlist
    template_name = 'myplaylists/playlist_detail.html'

class PlaylistCreate(CreateView):
    model = Playlist
    template_name = 'myplaylists/form.html'
    form_class = PlaylistForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PlaylistCreate, self).form_valid(form)






