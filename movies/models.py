from django.db import models


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
