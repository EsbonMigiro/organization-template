from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    UserRegistrationView,
    UserLoginView,
    UserProfileView,
)

urlpatterns = [
    path(
        'register/',
        UserRegistrationView.as_view(),
        name='register'),

    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/',
         UserProfileView.as_view({'get': 'retrieve',
                                  'patch': 'update'}),
         name='profile'),

        ]