import os

from django.http import FileResponse, HttpResponse
from wsgiref.util import FileWrapper

from rest_framework import viewsets
from rest_framework.decorators import detail_route

from .models import Song, Artist, Album
from .serializers import SongSerializer, AlbumSerializer, ArtistSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    @detail_route(url_path='stream/(?P<seek>\d+)',methods=['GET'])
    def stream(self, request, pk=None, seek=None):
        if not seek:
            return HttpResponse()

        seek = int(seek)
        
        if seek < 0 or seek >= 100:
            return HttpResponse()

        song = self.queryset.get(pk=pk)

        filesize = os.stat(song.audio_file.path).st_size
        _file = open(song.audio_file.path, 'rb')

        if not seek == 0:
            _file.seek(int((seek*(filesize))/100.0))

        return FileResponse(FileWrapper(_file, 8092), content_type='audio/mpeg')

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
