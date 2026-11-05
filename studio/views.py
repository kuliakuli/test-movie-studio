
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

from .models import Director, Actor, Movie, Role
from .forms import MovieForm


# ГЛАВНАЯ СТРАНИЦА
def home(request):
    context = {
        "directors": Director.objects.all(),
        "actors": Actor.objects.all(),
        "movies": Movie.objects.select_related("director").all(),
        "roles": Role.objects.select_related(
            "movie", "actor"
        ).all(),
    }

    return render(request, "studio/home.html", context)


# СПИСОК ФИЛЬМОВ
def movie_list(request):
    movies = Movie.objects.select_related("director").all()

    return render(request, "studio/movie_list.html", {
        "movies": movies
    })


# ПОДРОБНОСТИ ФИЛЬМА
def movie_detail(request, pk):
    movie = get_object_or_404(
        Movie.objects.select_related("director"),
        pk=pk
    )

    roles = Role.objects.filter(
        movie=movie
    ).select_related("actor")

    return render(request, "studio/movie_detail.html", {
        "movie": movie,
        "roles": roles
    })


# ПОИСК АКТЁРОВ ЧЕРЕЗ GET
def actor_search(request):
    name = request.GET.get("name", "").strip()

    actors = Actor.objects.all()

    if name:
        actors = actors.filter(
            Q(full_name__icontains=name)
        )

    return render(request, "studio/actor_search.html", {
        "actors": actors,
        "name": name
    })


# ДОБАВЛЕНИЕ ФИЛЬМА ЧЕРЕЗ POST
def movie_create(request):
    if request.method == "POST":
        form = MovieForm(request.POST)

        if form.is_valid():
            movie = form.save()

            return redirect("movie_detail", pk=movie.pk)

    else:
        form = MovieForm()

    return render(request, "studio/movie_form.html", {
        "form": form
    })
