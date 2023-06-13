from rest_framework.views import APIView, Request, Response, status

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
