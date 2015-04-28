from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.
# Create your views here.

from django.views.generic.base import TemplateResponseMixin
from django.views.generic import DetailView, DeleteView, ListView
from django.views.generic.edit import CreateView
from django.contrib.auth import logout

from models import Artist, Release, Song, Playlist
from forms import PlaylistForm


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
    context_object_name='latest_playlist_list'
    template_name='myplaylists/playlist_list.html'


class PlaylistDetail(DetailView, ConnegResponseMixin):
    model = Playlist
    template_name = 'myplaylists/playlist_detail.html'


class ReleaseDetail(DetailView):
    model = Release
    template_name = 'myplaylists/release_detail.html'


class ArtistDetail(DetailView):
    model = Artist
    template_name = 'myplaylists/artist_detail.html'


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


