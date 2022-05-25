from django.urls import path
from movie import views

app_name = "movie"
urlpatterns = [
    path('', views.index, name="index-movie"),
    path('create/', views.create, name="create-movie"),
    path('edit/<int:movie_id>', views.edit, name="edit-movie"),
    #path('update/<int:movie_id>', views.update, name="update-movie"),
    #path('delete/<int:movie_id>', views.delete, name="delete-movie"),
]
