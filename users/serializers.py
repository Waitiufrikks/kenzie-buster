from rest_framework import serializers
from users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class UserSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField(max_length=127)
    password = serializers.CharField(max_length=127, write_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.CharField(required=False)
    is_employee = serializers.BooleanField(required=False)
    is_superuser = serializers.BooleanField(read_only=True)

    def validate(self, data):
        email = data.get("email")
        username = data.get("username")

        if (
            User.objects.filter(email=email).exists()
            and User.objects.filter(username=username).exists()
        ):
            raise serializers.ValidationError(
                {
                    "username": ["username already taken."],
                    "email": ["email already registered."],
                }
            )

        return data

    def create(self, validated_data: dict) -> User:
        if validated_data.get("is_employee"):
            return User.objects.create_superuser(**validated_data)
        return User.objects.create_user(**validated_data)
