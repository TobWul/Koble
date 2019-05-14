from django.urls import path

from . import views

urlpatterns = [
    path('nytt-forslag', views.new_suggestion, name="suggestion")
]