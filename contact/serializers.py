from rest_framework import serializers

from contact import models


class ContactSerializer(serializers.ModelSerializer):
    """Serialize and deserializ contact information"""
    author_id = serializers.IntegerField(source='author.id',
                                         read_only=True)

    class Meta:
        model = models.Contact
        fields = ('id', 'name', 'email', 'phone', 'address', 'author_id')
