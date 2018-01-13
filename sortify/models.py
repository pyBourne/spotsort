from django.db import models


class Song(models.Model):
    spotify_id = models.CharField(null=False)
    acousticness = models.FloatField()
    analysis_url = models.URLField()
    danceability = models.FloatField()
    duration_ms = models.IntegerField()
    energy = models.FloatField()
    instrumentalness = models.FloatField()
    key = models.IntegerField()
    liveness = models.FloatField()
    loudness = models.FloatField()
    mode = models.IntegerField()
    speechiness = models.FloatField()
    tempo = models.FloatField()
    time_signature = models.IntegerField()
    track_href = models.URLField()
    valence = models.FloatField()
