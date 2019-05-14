from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from gym.models import Gym


def search(request):
    q = request.GET.get('q')
    print(q)
    context = {
        'q': q,
        'gym_results': Gym.objects.filter(Q(name__icontains=q) |
                                          Q(positive_filter__name__icontains=q) |
                                          Q(negative_filter__name__icontains=q) |
                                          Q(address__icontains=q)).distinct()
    }
    return render(request, 'home/search-results.html', context)
