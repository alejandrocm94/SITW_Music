from django.conf.urls import patterns, url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView

from models import Artist, Release, Song, Playlist
from forms import ArtistForm, SongForm, PlaylistForm
from views import PlaylistDetail, PlaylistCreate

urlpatterns = patterns('',
    # List all user playlist: /myplaylist/
    url(r'^$',
        ListView.as_view(
            queryset = Playlist.objects.all(),
            context_object_name='latest_playlist_list',
            template_name='myplaylists/playlist_list.html'),
            name='playlist'),

    # Restaurant details, ex.: /myplaylists/playlist/1/
    url(r'^playlist/(?P<pk>\d+)/$',
        PlaylistDetail.as_view(),
        name='playlist_detail'),

    # Create a restaurant: /myplaylists/playlist/create/
    url(r'^playlist/create/$',
        PlaylistCreate.as_view(),
        name='playlist_create'),

    # Edit restaurant details, ex: /myplaylists/playlist/1/edit/
    url(r'^playlist/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Playlist,
            form_class=PlaylistForm,
            template_name='myplaylists/form.html'),
            name='playlist_edit'),


    )
