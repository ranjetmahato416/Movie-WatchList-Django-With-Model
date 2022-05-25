from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie
from .forms import CreateMovie
def index(request):
    movies = Movie.objects.all().order_by('movie_title', 'actor', 'genre', 'release_date', 'imdb')
    return render(request,'movie/index.html', {'movies': movies})

def create(request):
    form = CreateMovie()
    if request.method == 'POST':
        form = CreateMovie(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie.index-branch')
        else:
            form = form.CreateMovie()
    return render(request, 'movie/create.html', {'form': form})
def edit(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'movie/edit.html', {'movie': movie})

def update(request, movie_id):
    branch = Movie.objects.get(id=movie_id)
    form = form.CreateMovie(request.POST, instance=Movie)
    if form.is_valid():
        form.save()
        return redirect('movie:index-movie')
    return render(request, 'movie/edit.html', {'movie':Movie})
def delete(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    movie.delete()
    return redirect('movie:index-movie')