from django.shortcuts import render

# Create your views here.
from gym.models import Gym


def gyms(request):
    context = {
        'gyms': Gym.objects.all
    }
    return render(request, 'gym/gym-page.html', context)