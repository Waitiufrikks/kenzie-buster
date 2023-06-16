from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response, status

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from movies.models import Movie
from movies.permission import CustomPermission
from movies.serializers import MovieSerializers, MovieOrderSerializers
from users.models import User


class MovieView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [CustomPermission]

    def get(self, request: Request) -> Response:
        movies = Movie.objects.all()
        serializers = MovieSerializers(movies, many=True)

        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        new_movie = request.data

        serializers = MovieSerializers(data=new_movie)
        serializers.is_valid(raise_exception=True)
        serializers.save(user=request.user)

        return Response(serializers.data, status=status.HTTP_201_CREATED)


class MovieDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [CustomPermission]

    def get(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        serializers = MovieSerializers(instance=movie)

        return Response(serializers.data, status=status.HTTP_200_OK)

    def delete(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, movie_id) -> Response:
        new_buy = request.data

        serializers = MovieOrderSerializers(data=new_buy)
        serializers.is_valid(raise_exception=True)
        movie_bought = get_object_or_404(Movie, id=movie_id)

        buyed_by_user = request.user

        serializers.save(buyed_by=buyed_by_user, movie=movie_bought)
        return Response(serializers.data, status=status.HTTP_201_CREATED)
