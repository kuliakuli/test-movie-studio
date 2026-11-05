
from django.db import models


# РЕЖИССЁР
class Director(models.Model):
    full_name = models.CharField(
        max_length=200,
        verbose_name="ФИО режиссёра"
    )

    date_of_birth = models.DateField(
        verbose_name="Дата рождения"
    )

    awards = models.TextField(
        blank=True,
        verbose_name="Награды"
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Режиссёр"
        verbose_name_plural = "Режиссёры"
        ordering = ["full_name"]


# АКТЁР
class Actor(models.Model):
    full_name = models.CharField(
        max_length=200,
        verbose_name="ФИО актёра"
    )

    date_of_birth = models.DateField(
        verbose_name="Дата рождения"
    )

    citizenship = models.CharField(
        max_length=100,
        verbose_name="Гражданство"
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Актёр"
        verbose_name_plural = "Актёры"
        ordering = ["full_name"]


# ФИЛЬМ
class Movie(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Название фильма"
    )

    year = models.PositiveIntegerField(
        verbose_name="Год выпуска"
    )

    genre = models.CharField(
        max_length=100,
        verbose_name="Жанр"
    )

    budget = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        verbose_name="Бюджет"
    )

    description = models.TextField(
        verbose_name="Описание"
    )

    director = models.ForeignKey(
        Director,
        on_delete=models.PROTECT,
        related_name="movies",
        verbose_name="Режиссёр"
    )

    def __str__(self):
        return f"{self.title} ({self.year})"

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
        ordering = ["-year", "title"]


# РОЛЬ
class Role(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="roles",
        verbose_name="Фильм"
    )

    actor = models.ForeignKey(
        Actor,
        on_delete=models.PROTECT,
        related_name="roles",
        verbose_name="Актёр"
    )

    role_name = models.CharField(
        max_length=200,
        verbose_name="Название роли"
    )

    def __str__(self):
        return (
            f"{self.actor.full_name} — "
            f"{self.role_name} ({self.movie.title})"
        )

    class Meta:
        verbose_name = "Роль"
        verbose_name_plural = "Роли"
