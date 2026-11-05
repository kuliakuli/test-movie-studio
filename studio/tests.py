
from datetime import date
from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from .models import Actor, Director, Movie, Role


class StudioViewsTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.director = Director.objects.create(
            full_name="Тестовый режиссёр",
            date_of_birth=date(1970, 1, 1),
            awards="Премия"
        )

        cls.actor = Actor.objects.create(
            full_name="Тестовый актёр",
            date_of_birth=date(1990, 5, 10),
            citizenship="Россия"
        )

        cls.movie = Movie.objects.create(
            title="Тестовый фильм",
            year=2024,
            genre="Драма",
            budget=Decimal("1000000.00"),
            description="Описание тестового фильма",
            director=cls.director
        )

        Role.objects.create(
            movie=cls.movie,
            actor=cls.actor,
            role_name="Главный герой"
        )

    def test_home_page(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Тестовый фильм")

    def test_movie_list(self):
        response = self.client.get(reverse("movie_list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Тестовый фильм")

    def test_movie_detail(self):
        response = self.client.get(
            reverse("movie_detail", args=[self.movie.pk])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Главный герой")
        self.assertContains(response, "Тестовый актёр")

    def test_movie_not_found(self):
        response = self.client.get(
            reverse("movie_detail", args=[99999])
        )

        self.assertEqual(response.status_code, 404)

    def test_actor_search(self):
        response = self.client.get(
            reverse("actor_search"),
            {"name": "Тестовый"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Тестовый актёр")

    def test_movie_create_get(self):
        response = self.client.get(reverse("movie_create"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Сохранить фильм")

    def test_movie_create_post(self):
        response = self.client.post(
            reverse("movie_create"),
            {
                "title": "Новый фильм",
                "year": 2025,
                "genre": "Фантастика",
                "budget": "5000000.00",
                "description": "Новый тестовый фильм",
                "director": self.director.pk,
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Movie.objects.filter(title="Новый фильм").exists()
        )
