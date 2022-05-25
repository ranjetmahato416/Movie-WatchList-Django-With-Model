from django import forms
from .import models
class CreateMovie(forms.ModelForm):
    class Meta:
        model = models.Movie
        fields = ['actor', 'movie_title', 'genre', 'release_date', 'imdb']