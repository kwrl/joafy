from rest_framework import serializers

from .models import Song, Artist, Album

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'name', 'track', 'album', 'artist')

class ArtistSerializer(serializers.ModelSerializer):
    albums = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Artist
        fields = ('id', 'name', 'albums')


class AlbumSerializer(serializers.ModelSerializer):
    songs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Album
        fields = ('id', 'name', 'artist', 'songs')
