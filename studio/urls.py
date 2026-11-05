
from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),

    path(
        "movies/",
        views.movie_list,
        name="movie_list"
    ),

    path(
        "movies/create/",
        views.movie_create,
        name="movie_create"
    ),

    path(
        "movies/<int:pk>/",
        views.movie_detail,
        name="movie_detail"
    ),

    path(
        "actors/",
        views.actor_search,
        name="actor_search"
    ),
]
