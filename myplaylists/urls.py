from django.conf.urls import patterns, url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView, DeleteView

from models import Artist, Release, Song, Playlist
from forms import ArtistForm, SongForm, PlaylistForm
from views import PlaylistDetail, PlaylistCreate, PlaylistDelete, ReleaseDetail, ArtistDetail, SongDetail, PlaylistList, \
    ReleaseList, ArtistList, SongList

urlpatterns = patterns('',

    # List all user playlist: /myplaylists/
    url(r'^playlists/$',
        PlaylistList.as_view(),
        name='playlist'),

    # List all user playlist: /myplaylists/playlists.json
    url(r'^playlists\.(?P<extension>(json|xml))$',
        PlaylistList.as_view(),
        name='playlist_conneg'),



    # Playlist details, ex.: /myplaylists/playlists/1
    url(r'^playlists/(?P<pk>\d+)/$',
        PlaylistDetail.as_view(),
        name='playlist_detail'),

    # Playlist details, ex.: /myplaylists/playlists/1.json
    url(r'^playlists/(?P<pk>\d+)\.(?P<extension>(json|xml))$',
        PlaylistDetail.as_view(),
        name='playlist_detail_conneg'),



    # Create a playlist: /myplaylists/playlists/create/
    url(r'^playlists/create/$',
        PlaylistCreate.as_view(),
        name='playlist_create'),

    # Edit playlist details, ex: /myplaylists/playlists/edit/1
    url(r'^playlists/edit/(?P<pk>\d+)/$',
        UpdateView.as_view(
            model=Playlist,
            form_class=PlaylistForm,
            template_name='myplaylists/form.html'),
            name='playlist_edit'),

    # Delete playlist, ex: /myplaylists/playlists/delete/1
    url(r'^playlists/delete/(?P<pk>\d+)/$',
        PlaylistDelete.as_view(),
        name='delete_playlist'),



    # List all releases: myplaylists/releases/
    url(r'^releases/$',
        ReleaseList.as_view(),
        name='releases'),

    # List all releases: /myplaylists/releases.json
    url(r'^releases\.(?P<extension>(json|xml))$',
        ReleaseList.as_view(),
        name='releases_conneg'),



    #Release details, ex: /myplaylists/release/1
    url(r'^releases/(?P<pk>\d+)/$',
        ReleaseDetail.as_view(),
        name='release_detail'),

    # Release details, ex.: /myplaylists/releases/1.json
    url(r'^releases/(?P<pk>\d+)\.(?P<extension>(json|xml))$',
        ReleaseDetail.as_view(),
        name='release_detail_conneg'),



    # List all Artists: myplaylists/artists/
    url(r'^artists/$',
        ArtistList.as_view(),
        name='artists'),

    # List all Artists: /myplaylists/releases.json
    url(r'^artists\.(?P<extension>(json|xml))$',
        ArtistList.as_view(),
        name='artists_conneg'),



    # Artist details, ex: /myplaylists/artist/1
    url(r'^artist/(?P<pk>\d+)/$',
        ArtistDetail.as_view(),
        name='artist_detail'),

    # Artist details, ex.: /myplaylists/releases/1.json
    url(r'^artist/(?P<pk>\d+)\.(?P<extension>(json|xml))$',
        ArtistDetail.as_view(),
        name='artist_detail_conneg'),



    # List all Songs: myplaylists/songs/
    url(r'^songs/$',
        SongList.as_view(),
        name='songs'),

    # List all songs: /myplaylists/songs.json
    url(r'^songs\.(?P<extension>(json|xml))$',
        ArtistList.as_view(),
        name='songs_conneg'),



    # Song details, ex: /myplaylists/songs/1
    url(r'^songs/(?P<pk>\d+)/$',
        SongDetail.as_view(),
        name='song_detail'),

    # Song details, ex.: /myplaylists/releases/1.json
    url(r'^songs/(?P<pk>\d+)\.(?P<extension>(json|xml))$',
        SongDetail.as_view(),
        name='song_detail_conneg'),

    )