from django.db import models


# Create your models here.
class Movie(models.Model):
    actor = models.CharField(max_length=30)
    movie_title = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    release_date = models.CharField(max_length=10)
    imdb = models.CharField(max_length=10)

    def __str__(self):
        return self.movie_title


class Song(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=50)
    song_title = models.CharField(max_length=100)
