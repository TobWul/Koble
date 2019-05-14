from django.urls import path

from . import views

urlpatterns = [
    path('treningssenter', views.gyms, name="gyms"),
]