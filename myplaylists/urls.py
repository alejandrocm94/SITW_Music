from django.conf.urls import patterns, url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView, DeleteView

from models import Artist, Release, Song, Playlist
from forms import ArtistForm, SongForm, PlaylistForm
from views import PlaylistDetail, PlaylistCreate, PlaylistDelete, ReleaseDetail, ArtistDetail, SongDetail, PlaylistList

urlpatterns = patterns('',
    # List all user playlist: /myplaylists/
    url(r'^playlists/$',
        PlaylistList.as_view(),
        name='playlist'),

    # List all user playlist: /myplaylists/playlists.json
    url(r'^playlists\.(?P<extension>(json|xml))$',
        PlaylistList.as_view(),
        name='playlist_conneg'),

    # Playlist details, ex.: /myplaylists/playlisty1
    url(r'^playlists/(?P<pk>\d+)/$',
        PlaylistDetail.as_view(),
        name='playlist_detail'),

    url(r'^playlists/(?P<pk>\d+)\.(?P<extension>(json|xml))$',
        PlaylistDetail.as_view(),
        name='playlist_detail_conneg'),


    # Create a playlist: /myplaylists/create/
    url(r'^playlists/create/$',
        PlaylistCreate.as_view(),
        name='playlist_create'),

    # Edit playlist details, ex: /myplaylists/edit/1
    url(r'^playlists/edit/(?P<pk>\d+)/$',
        UpdateView.as_view(
            model=Playlist,
            form_class=PlaylistForm,
            template_name='myplaylists/form.html'),
            name='playlist_edit'),

    # Delete playlist, ex: /myplaylists/delete/1
    url(r'^playlists/delete/(?P<pk>\d+)/$',
        PlaylistDelete.as_view(),
        name='delete_playlist'),

    #Release details, ex: /myplaylists/release/1
    url(r'^releases/(?P<pk>\d+)/$',
        ReleaseDetail.as_view(),
        name='release_detail'),

    #Artist details, ex: /myplaylists/artist/1
    url(r'^artist/(?P<pk>\d+)/$',
        ArtistDetail.as_view(),
        name='artist_detail'),

    #Song details, ex: /myplaylists/song/1
    url(r'^song/(?P<pk>\d+)/$',
        SongDetail.as_view(),
        name='song_detail'),
    )



