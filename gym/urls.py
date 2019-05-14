from django.urls import path

from . import views

urlpatterns = [
    path('treningssenter', views.gyms, name="gyms"),
    path('treningssenter/<slug:gym_slug>', views.gym_detail, name="gym_detail")
]