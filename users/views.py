from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response, status

from rest_framework_simplejwt.authentication import JWTAuthentication
from .permission import CustomPermission

from users.models import User
from users.serializers import UserSerializers


class UserView(APIView):
    def get(self, request: Request) -> Response:
        users = User.objects.all()
        serializer = UserSerializers(users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        print(request.data)
        # username_exist = User.objects.filter(username=request.data.username)
        serializer = UserSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [CustomPermission]

    def get(self, request: Request, user_id) -> Response:
        movie = get_object_or_404(User, id=user_id)
        serializers = UserSerializers(instance=movie)

        return Response(serializers.data, status=status.HTTP_200_OK)

    def patch(self, request: Request, user_id) -> Response:
        user = get_object_or_404(User, id=user_id)
        serializers = UserSerializers(instance=user, data=request.data, partial=True)
        serializers.is_valid(raise_exception=True)

        serializers.save()

        return Response(serializers.data, status=status.HTTP_200_OK)
