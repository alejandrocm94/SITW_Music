from django.contrib.auth.models import User, Group
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
# Create your views here.

from django.views.generic.base import TemplateResponseMixin
from django.views.generic import DetailView, DeleteView, ListView
from django.views.generic.edit import CreateView
from django.contrib.auth import logout

from models import Artist, Release, Song, Playlist
from forms import PlaylistForm

from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from myplaylists.serializers import UserSerializer, SongSerializer, SongSerializer, ArtistSerializer, ReleaseSerializer, \
    PlaylistSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    model = User
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    model = User
    serializer_class = UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SongList(generics.ListCreateAPIView):
    model = Song
    serializer_class = SongSerializer


class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Song
    serializer_class = SongSerializer
    name = "song-detail"


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class ArtistList(generics.ListCreateAPIView):
    model = Artist
    serializer_class = ArtistSerializer


class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Artist
    serializer_class = ArtistSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ReleaseList(generics.ListCreateAPIView):
    model = Release
    serializer_class = ReleaseSerializer


class ReleaseDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Artist
    serializer_class = ReleaseSerializer


class ReleaseViewSet(viewsets.ModelViewSet):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer


class PlaylistList(generics.ListCreateAPIView):
    model = Playlist
    serializer_class = PlaylistSerializer
    lookup_field = 'songs'


class PlaylistDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Playlist
    serializer_class = PlaylistSerializer
    lookup_field = 'songs'


class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    lookup_field = 'songs'


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


