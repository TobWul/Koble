from django.urls import path
from django.views.generic import TemplateView

from home import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='home/index.html'), name="home"),
    path('search', views.search, name="search")
]