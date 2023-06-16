from rest_framework import serializers

from movies.models import Movie, Rating_Age, MovieOrder


class MovieSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, default=None, required=False)
    rating = serializers.ChoiceField(
        choices=Rating_Age.choices, default=Rating_Age.Rated_G
    )
    synopsis = serializers.CharField(default=None, required=False)
    added_by = serializers.EmailField(source="user.email", read_only=True)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)


class MovieOrderSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(source="movie.title", read_only=True)
    buyed_at = serializers.DateTimeField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_by = serializers.EmailField(source="buyed_by.email", read_only=True)


    def create(self, validated_data):
        return MovieOrder.objects.create(**validated_data)
