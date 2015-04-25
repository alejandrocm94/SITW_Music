from django.conf.urls import patterns, url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView, DeleteView

from models import Artist, Release, Song, Playlist
from forms import ArtistForm, SongForm, PlaylistForm
from views import PlaylistDetail, PlaylistCreate, PlaylistDelete, ReleaseDetail

urlpatterns = patterns('',
    # List all user playlist: /myplaylists/
    url(r'^$',
        ListView.as_view(
            queryset = Playlist.objects.all(),
            context_object_name='latest_playlist_list',
            template_name='myplaylists/playlist_list.html'),
            name='playlist'),

    # Playlist details, ex.: /myplaylists/1
    url(r'^(?P<pk>\d+)/$',
        PlaylistDetail.as_view(),
        name='playlist_detail'),


    # Create a playlist: /myplaylists/create/
    url(r'^create/$',
        PlaylistCreate.as_view(),
        name='playlist_create'),

    # Edit playlist details, ex: /myplaylists/edit/1
    url(r'^edit/(?P<pk>\d+)/$',
        UpdateView.as_view(
            model=Playlist,
            form_class=PlaylistForm,
            template_name='myplaylists/form.html'),
            name='playlist_edit'),

    # Delete playlist, ex: /myplaylists/delete/1
    url(r'^delete/(?P<pk>\d+)/$',
        PlaylistDelete.as_view(),
        name='delete_playlist'),

    url(r'^release/(?P<pk>\d+)/$',
        ReleaseDetail.as_view(),
        name='release_detail'),
    )



