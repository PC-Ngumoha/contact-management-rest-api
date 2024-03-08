from django.conf import settings
from django.db import models


class Contact(models.Model):
    """A contact item"""
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=60)
    address = models.TextField()

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        """String representation of contact"""
        return self.email