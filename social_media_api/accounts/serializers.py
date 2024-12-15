from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    # Explicitly define CharField for password fields
    username = serializers.CharField(max_length=150, required=True)
    email = serializers.CharField(max_length=255, required=True)
    password = serializers.CharField(
        write_only=True, required=True, style={'input_type': 'password'}
    )
    confirm_password = serializers.CharField(
        write_only=True, required=True, style={'input_type': 'password'}
    )
    bio = serializers.CharField(max_length=500, required=False, allow_blank=True)
    profile_picture = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'confirm_password', 'bio', 'profile_picture']

    def validate(self, data):
        """
        Validate that password and confirm_password fields match.
        """
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        """
        Create a new user and generate a token for authentication.
        """
        # Remove confirm_password before passing data to user creation
        validated_data.pop('confirm_password')

        # Use get_user_model().objects.create_user to create a user
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture')
        )

        # Generate a token for the user
        Token.objects.create(user=user)

        return user


class UserLoginSerializer(serializers.Serializer):
    """
    Serializer for user login.
    """
    username = serializers.CharField(required=True)
    password = serializers.CharField(
        write_only=True, required=True, style={'input_type': 'password'}
    )


class TokenSerializer(serializers.ModelSerializer):
    """
    Serializer for Token model to return user token.
    """
    class Meta:
        model = Token
        fields = ['key', 'user']
