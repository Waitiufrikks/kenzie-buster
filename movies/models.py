from django.db import models

from users.models import User


class Rating_Age(models.TextChoices):
    Rated_G = "G"
    Rated_PG = "PG"
    Rated_PG_13 = "PG-13"
    Rated_R = "R"
    Rated_NC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, blank=True, default=None)
    rating = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=Rating_Age.choices,
        default=Rating_Age.Rated_G,
    )
    synopsis = models.TextField(null=True, blank=True, default=None)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="movies"
    )
    buyed_by = models.ManyToManyField(
        "users.User", through="movies.MovieOrder", related_name="buyed_movies"
    )

    def __str__(self) -> str:
        return f"id: {self.id} ,title: {self.title}"


class MovieOrder(models.Model):
    movie = models.ForeignKey("movies.Movie", on_delete=models.CASCADE)
    buyed_by = models.ForeignKey("users.User", on_delete=models.CASCADE)
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self) -> str:
        return f"user: {self.user} ,movie: {self.movie},buyed:{self.buyed_at},"
