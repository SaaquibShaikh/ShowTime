# from django.conf.urls import re_path
from django.urls import path, re_path
from . import views

# We added namespace for our app
app_name = 'api'

urlpatterns = [
    path('movies/<city_name>', views.movies_in_city, name="movies_in_city"),
    re_path('movies', views.all_movies, name="movies"),
    path('book/<city_name>/<movie_name>/<theatre_name>/<show_name>', views.book_ticket, name="book_ticket"),
    path('shows/<movie_name>/<city_name>',views.available_shows_for_movie,name="shows_of_movie_in_city"),
    re_path('cities', views.all_cities, name="cities"),
    re_path('login', views.user_login, name="login"),
    re_path('logout', views.user_logout, name="logout"),
    re_path('registration', views.user_registration, name="registration"),
]
