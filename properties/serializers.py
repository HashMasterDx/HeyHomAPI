from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Property, CustomUser


# Property serializer
class PropertySerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100, validators=[UniqueValidator(queryset=Property.objects.all())])

    class Meta:
        model = Property
        fields = (
            'id', 'title', 'description', 'price', 'location', 'property_type', 'bedrooms', 'bathrooms', 'square_feet',
            'available')


class TokenPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['email'] = user.email

        return token


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=CustomUser.objects.all())])
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
