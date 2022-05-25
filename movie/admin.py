from django.contrib import admin
from movie.models import Movie
from movie.models import Song
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display=('movie_title','genre','actor','release_date', 'imdb')
    list_filter=['genre', 'release_date']
    search_fields=['movie_title','actor','genre']
   

admin.site.register(Movie, MovieAdmin)
admin.site.register(Song)

