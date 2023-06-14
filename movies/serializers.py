from rest_framework import serializers
from users.serializers import UserSerializers
from movies.models import Movie, Rating_Age


class MovieSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, default=None, required=False)
    rating = serializers.CharField(max_length=20, required=False)
    synopsis = serializers.CharField(default=None, required=False)
    added_by = serializers.EmailField(source="user.email", read_only=True)

    def validate_rating(self, value):
        if value and value not in Rating_Age.choices:
            raise serializers.ValidationError(
                f'"{value}" is not a valid choice for rating.'
            )
        return value

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
