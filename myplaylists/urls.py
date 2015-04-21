from django.conf.urls import patterns, url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView, DeleteView

from models import Artist, Release, Song, Playlist
from forms import ArtistForm, SongForm, PlaylistForm
from views import PlaylistDetail, PlaylistCreate, PlaylistDelete

urlpatterns = patterns('',
    # List all user playlist: /myplaylist/
    url(r'^$',
        ListView.as_view(
            queryset = Playlist.objects.all(),
            context_object_name='latest_playlist_list',
            template_name='myplaylists/playlist_list.html'),
            name='playlist'),

    # Playlist details, ex.: /myplaylists/1/
    url(r'^(?P<pk>\d+)/$',
        PlaylistDetail.as_view(),
        name='playlist_detail'),

    # Create a playlist: /myplaylists/create/
    url(r'^create/$',
        PlaylistCreate.as_view(),
        name='playlist_create'),

    # Edit playlist details, ex: /myplaylists/1/edit/
    url(r'^(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Playlist,
            form_class=PlaylistForm,
            template_name='myplaylists/form.html'),
            name='playlist_edit'),

    # Delete playlist, ex: /myplaylists/1/delete/
    url(r'^(?P<pk>\d+)/delete/$',
        PlaylistDelete.as_view(),
        name='playlist_delete'),
    )
