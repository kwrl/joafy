from django.db import models

class Artist(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.TextField()
    artist = models.ForeignKey(Artist, related_name='albums')

    def __str__(self):
        return self.name

    class Meta:
        unique_together = (('name', 'artist'),)

class Song(models.Model):
    name = models.TextField()

    track = models.PositiveIntegerField()
    artist = models.ForeignKey(Artist)
    album = models.ForeignKey(Album, related_name='songs')

    audio_file = models.FileField()

    def __str__(self):
        return self.name

    class Meta:
        unique_together = (('track', 'album'),)
