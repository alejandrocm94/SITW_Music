from django.conf.urls import patterns, url, include
from django.views.generic import UpdateView
from models import Playlist
from forms import PlaylistForm
from views import PlaylistDetail, PlaylistCreate, PlaylistDelete, ReleaseDetail, ArtistDetail, SongDetail, \
    PlaylistList, ReleaseList, ArtistList, SongList, search, APIUserViewSet, APISongViewSet, APIArtistViewSet, \
    mainpage, APIReleaseViewSet, APIPlaylistViewSet, UserProfileCreate, UserProfileDetail, UserProfile, UserProfileForm
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', APIUserViewSet)
router.register(r'artists', APIArtistViewSet)
router.register(r'songs', APISongViewSet)
router.register(r'releases', APIReleaseViewSet)
router.register(r'playlists', APIPlaylistViewSet)

urlpatterns = patterns('',

    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', mainpage, name='home'),
    # List all user playlist: /myplaylists/
    url(r'^playlists/$', PlaylistList.as_view(), name='playlist'),
    # Playlist details, ex.: /myplaylists/playlists/1
    url(r'^playlists/(?P<pk>\d+)/$', PlaylistDetail.as_view(), name='playlist_detail'),
    # Create a playlist: /myplaylists/playlists/create/
    url(r'^playlists/create/$', PlaylistCreate.as_view(), name='playlist_create'),
    # Edit playlist details, ex: /myplaylists/playlists/edit/1
    url(r'^playlists/edit/(?P<pk>\d+)/$', UpdateView.as_view(
        model=Playlist,
        form_class=PlaylistForm,
        template_name='myplaylists/form.html'),
        name='playlist_edit'),
    # Delete playlist, ex: /myplaylists/playlists/delete/1
    url(r'^playlists/delete/(?P<pk>\d+)/$', PlaylistDelete.as_view(), name='delete_playlist'),
    # List all releases: myplaylists/releases/
    url(r'^releases/$', ReleaseList.as_view(), name='releases'),
    # Release details, ex: /myplaylists/releases/1
    url(r'^releases/(?P<pk>\d+)/$', ReleaseDetail.as_view(), name='release_detail'),
    # List all Artists: myplaylists/artists/
    url(r'^artists/$', ArtistList.as_view(), name='artists'),
    # Artist details, ex: /myplaylists/artists/1
    url(r'^artists/(?P<pk>\d+)/$', ArtistDetail.as_view(), name='artist_detail'),
    # List all Songs: myplaylists/songs/
    url(r'^songs/$', SongList.as_view(), name='songs'),
    # Song details, ex: /myplaylists/songs/1
    url(r'^songs/(?P<pk>\d+)/$', SongDetail.as_view(), name='song_detail'),
    url(r'^songs/search/$', search, name="song_search"),
    # User profile details, ex: /myplaylists/user/1/userprofile/
    url(r'^user/(?P<pk>\d+)/userprofile/$', UserProfileDetail.as_view(), name='userprofile_detail'),
    # Create a User profile: /myplaylists/user/1/userprofile/create/
    url(r'^user/(?P<pk>\d+)/userprofile/create/$', UserProfileCreate.as_view(), name='userprofile_create'),
    # Edit User profile details, ex: /myplaylists/user/1/userprofile/edit/1
    url(r'^user/(?P<pk>\d+)/userprofile/edit/(?P<id>\d+)/$', UpdateView.as_view(
        model=UserProfile,
        form_class=UserProfileForm,
        template_name='myplaylists/form.html'),
        name='userprofile_edit'),
    url(r'^releases/(?P<pk>\d+)/reviews/create/$', 'myplaylists.views.review', name='review_create'),
    )

