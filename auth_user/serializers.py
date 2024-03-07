from rest_framework import serializers
from auth_user import models


class UserSerializer(serializers.ModelSerializer):
    """Serializes and deserializes user instances"""

    class Meta:
        model = models.User
        fields = ('email', 'name', 'created_on', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            }
        }

    def create(self, validated_data):
        """Create user instance from serializer"""
        user = models.User.objects.create_user(
            email=validated_data.get('email'),
            name=validated_data.get('name'),
            password=validated_data.get('password')
        )
        return user
    
    def update(self, instance, validated_data):
        """Updates the details of a user instance from serializer"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)