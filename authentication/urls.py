from django.contrib.auth import logout
from django.urls import path, include
from django.conf import settings

from . import views

urlpatterns = [
    path('oauth', include('social_django.urls', namespace='social')),
    path('register/', views.RegisterFormView.as_view(), name='register'),
    path('login/', views.LoginFormView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
]