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
from myplaylists.serializers import UserSerializer, SongSerializer, SongSerializer, ArtistSerializer


@api_view(['GET'])
def api_root(request, format=None):
    """
    The entry endpoint of our API
    """
    return Response({
        'users': reverse('user-list', vrequest=request),
        'songs': reverse('song-list', request=request),
    })


class UserList(generics.ListCreateAPIView):
    """
      API endpoint that	represents a list of users
    """
    queryset = User.objects.all()
    model = User
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
      API endpoint that	represents a single users
    """
    model = User
    serializer_class = UserSerializer


class SongList(generics.ListCreateAPIView):
    """
      API endpoint that	represents a list of groups
    """
    model = Song
    serializer_class = SongSerializer


class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    """
      API endpoint that	represents a single group
    """
    model = Song
    serializer_class = SongSerializer


class ArtistList(generics.ListCreateAPIView):
    """
      API endpoint that	represents a list of groups
    """
    model = Artist
    serializer_class = ArtistSerializer


class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    """
      API endpoint that	represents a single group
    """
    model = Artist
    serializer_class = ArtistSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SongViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ConnegResponseMixin(TemplateResponseMixin):
    def render_json_object_response(self, objects, **kwargs):
        json_data = serializers.serialize(u"json", objects, **kwargs)
        return HttpResponse(json_data, content_type=u"application/json")

    def render_xml_object_response(self, objects, **kwargs):
        xml_data = serializers.serialize(u"xml", objects, **kwargs)
        return HttpResponse(xml_data, content_type=u"application/xml")

    def render_to_response(self, context, **kwargs):
        if 'extension' in self.kwargs:
            try:
                objects = [self.object]
            except AttributeError:
                objects = self.object_list

            if self.kwargs['extension'] == 'json':
                return self.render_json_object_response(objects=objects)
            elif self.kwargs['extension'] == 'xml':
                return self.render_xml_object_response(objects=objects)
        else:
            return super(ConnegResponseMixin, self).render_to_response(context)


class PlaylistList(ListView, ConnegResponseMixin):
    model = Playlist
    queryset = Playlist.objects.all()
    context_object_name = 'latest_playlist_list'
    template_name = 'myplaylists/playlist_list.html'


class PlaylistDetail(DetailView, ConnegResponseMixin):
    model = Playlist
    template_name = 'myplaylists/playlist_detail.html'


class ReleaseList(ListView, ConnegResponseMixin):
    model = Release
    queryset = Release.objects.all()
    context_object_name = 'all_releases_list'
    template_name = 'myplaylists/release_list.html'


class ReleaseDetail(DetailView, ConnegResponseMixin):
    model = Release
    template_name = 'myplaylists/release_detail.html'


class ArtistList(ListView, ConnegResponseMixin):
    model = Artist
    queryset = Artist.objects.all()
    context_object_name = 'all_artists_list'
    template_name = 'myplaylists/artist_list.html'


class ArtistDetail(DetailView, ConnegResponseMixin):
    model = Artist
    template_name = 'myplaylists/artist_detail.html'


class SongList(ListView, ConnegResponseMixin):
    model = Song
    queryset = Song.objects.all()
    context_object_name = 'all_songs_list'
    template_name = 'myplaylists/song_list.html'


class SongDetail(DetailView, ConnegResponseMixin):
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


