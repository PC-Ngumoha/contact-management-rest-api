from django.contrib.auth.models import (
  AbstractBaseUser, PermissionsMixin, BaseUserManager)
from django.db import models


class CustomUserManager(BaseUserManager):
    """Custom user manager"""
    def create_user(self, email, name, password=None):
        """Assists the process of creating a new regular user"""
        if not email:
            raise ValueError('\'Email\' field always required')
        if not name:
            raise ValueError('\'Name\' field always required')
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, name, password):
        """Assists the process of creating a superuser"""
        user = self.create_user(email, name, password)

        user.is_staff = True
        user.is_superuser = True
       
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user"""
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('name',)

    def get_full_name(self):
        """Return full (official) name for the user"""
        return self.name
    
    def get_short_name(self):
        """Return the short (unofficial) name for the user"""
        return self.name
    
    def __str__(self):
        """String representation for instance of the user"""
        return self.email
