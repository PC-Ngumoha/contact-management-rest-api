from django.urls import (path, include)
from rest_framework.routers import DefaultRouter

from auth_user import views

router = DefaultRouter()
router.register('user', views.UserProfileViewSet)

urlpatterns = (
    path('', include(router.urls)),
)