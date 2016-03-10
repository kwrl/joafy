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
    chunk_size = 512*1024
    
    @detail_route(url_path='stream/(?P<seek>\d+)',methods=['GET'])
    def stream(self, request, pk=None, seek=None):

        seek = float(seek)

        #Ensure that seek is a valid percentage
        if seek < 0 or seek >= 100:
            seek = 0

        song = self.queryset.get(pk=pk)

        filesize = os.stat(song.audio_file.path).st_size
        audio_file = open(song.audio_file.path, 'rb')

        if seek != 0:
            audio_file.seek(int((seek*(filesize))/100.0))

        #TODO: fix hardcoded content_type
        return FileResponse(FileWrapper(audio_file, self.chunk_size), content_type='audio/mpeg')

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
