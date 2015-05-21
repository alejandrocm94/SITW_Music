from django.contrib.auth.models import User, Group
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
# Create your views here.

from django.views.generic import DetailView, DeleteView, ListView
from django.views.generic.edit import CreateView
from django.contrib.auth import logout

from models import Artist, Release, Song, Playlist
from forms import PlaylistForm

from rest_framework import viewsets
from rest_framework import generics
from myplaylists.serializers import UserSerializer, SongSerializer, ArtistSerializer, ReleaseSerializer,\
    PlaylistSerializer


class APIUserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    model = User
    serializer_class = UserSerializer


class APIUserDetail(generics.RetrieveUpdateDestroyAPIView):
    model = User
    serializer_class = UserSerializer


class APIUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class APISongList(generics.ListCreateAPIView):
    model = Song
    serializer_class = SongSerializer


class APISongDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Song
    serializer_class = SongSerializer


class APISongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class APIArtistList(generics.ListCreateAPIView):
    model = Artist
    serializer_class = ArtistSerializer


class APIArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Artist
    serializer_class = ArtistSerializer


class APIArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class APIReleaseList(generics.ListCreateAPIView):
    model = Release
    serializer_class = ReleaseSerializer


class APIReleaseDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Artist
    serializer_class = ReleaseSerializer


class APIReleaseViewSet(viewsets.ModelViewSet):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer


class APIPlaylistList(generics.ListCreateAPIView):
    model = Playlist
    serializer_class = PlaylistSerializer


class APIPlaylistDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Playlist
    serializer_class = PlaylistSerializer


class APIPlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


class PlaylistList(ListView):
    model = Playlist
    queryset = Playlist.objects.all()
    context_object_name = 'latest_playlist_list'
    template_name = 'myplaylists/playlist_list.html'


class PlaylistDetail(DetailView):
    model = Playlist
    template_name = 'myplaylists/playlist_detail.html'


class ReleaseList(ListView):
    model = Release
    queryset = Release.objects.all()
    context_object_name = 'all_releases_list'
    template_name = 'myplaylists/release_list.html'


class ReleaseDetail(DetailView):
    model = Release
    template_name = 'myplaylists/release_detail.html'


class ArtistList(ListView):
    model = Artist
    queryset = Artist.objects.all()
    context_object_name = 'all_artists_list'
    template_name = 'myplaylists/artist_list.html'


class ArtistDetail(DetailView):
    model = Artist
    template_name = 'myplaylists/artist_detail.html'


class SongList(ListView):
    model = Song
    queryset = Song.objects.all()
    context_object_name = 'all_songs_list'
    template_name = 'myplaylists/song_list.html'


class SongDetail(DetailView):
    model = Song
    template_name = 'myplaylists/song_detail.html'


class PlaylistCreate(CreateView):
    model = Playlist
    template_name = 'myplaylists/form.html'
    form_class = PlaylistForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PlaylistCreate, self).form_valid(form)


class PlaylistDelete(DeleteView):
    model = Playlist
    success_url = '/myplaylists/playlists'


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


def search(request):
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        found_entries = Song.objects.filter(name__icontains=query_string)
        found_entries = found_entries | Song.objects.filter(release__name__icontains=query_string)
        found_entries = found_entries | Song.objects.filter(release__artist__name=query_string)

    return render_to_response('myplaylists/song_list.html',
                              {'all_songs_list': found_entries},
                              context_instance=RequestContext(request))


