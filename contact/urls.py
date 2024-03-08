from django.urls import (path, include)
from rest_framework.routers import DefaultRouter

from contact import views

router = DefaultRouter()
router.register('contacts', views.ContactInfoViewSet, basename='contacts')

urlpatterns = (
  path('', include(router.urls)),
)