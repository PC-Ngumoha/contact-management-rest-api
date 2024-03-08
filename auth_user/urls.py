from django.urls import (path, include)
from rest_framework.routers import DefaultRouter

from auth_user import views

router = DefaultRouter()
router.register('users', views.UserProfileViewSet)

urlpatterns = (
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('', include(router.urls)),
)