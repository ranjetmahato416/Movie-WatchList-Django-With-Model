from django.shortcuts import render
from movie.models import Movie


#Create your views here.

def index(request):
    moviesData = Movie.objects.all()
    data = {
        'moviesData': moviesData
    }
    # for m in moviesData:
    #     print(m.movie_title)
    return render(request, 'index.html', data)

def master(request):
    return render(request, 'master.html')
    