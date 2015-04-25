from django.shortcuts import render, render_to_response

# Create your views here.
# Create your views here.

from django.core import urlresolvers
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, DeleteView
from django.views.generic.edit import CreateView
from django.contrib.auth import logout

from models import Artist, Release, Song, Playlist
from forms import ArtistForm, ReleaseForm, SongForm, PlaylistForm

class PlaylistDetail(DetailView):
    model = Playlist
    template_name = 'myplaylists/playlist_detail.html'

class ReleaseDetail(DetailView):
    model = Release
    template_name = 'myplaylists/release_detail.html'

class PlaylistCreate(CreateView):
    model = Playlist
    template_name = 'myplaylists/form.html'
    form_class = PlaylistForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PlaylistCreate, self).form_valid(form)

class PlaylistDelete(DeleteView):
    model = Playlist
    success_url = '/myplaylists/'

def mainpage(request):
    return render_to_response(
        'myplaylists/mainpage.html',
        {
            'user': request.user
        }
    )

def log_out(request):
    logout(request)
    return render_to_response(
        'registration/logout.html'
    )


