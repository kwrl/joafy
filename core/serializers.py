from rest_framework import serializers

from .models import Song, Artist, Album

class SongSerializer(serializers.ModelSerializer):
    artist = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name='artist-detail')
    album = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name='album-detail')
    class Meta:
        model = Song
        fields = ('id', 'name', 'track', 'album', 'artist')

class ArtistSerializer(serializers.ModelSerializer):
    albums = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='album-detail')
    class Meta:
        model = Artist
        fields = ('id', 'name', 'albums')


class AlbumSerializer(serializers.ModelSerializer):
    artist = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name='artist-detail')
    songs = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='song-detail')
    class Meta:
        model = Album
        fields = ('id', 'name', 'artist', 'songs')
