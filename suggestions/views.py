from django.contrib.auth import get_user_model
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect

# Create your views here.
from authentication.models import Profile
from filters.models import Filter
from suggestions.forms import SuggestionForm


def new_suggestion(request):
    context = {
        'form': SuggestionForm(),
        'filters': Filter.objects.all()
    }
    if request.method == 'GET' and request.user.is_authenticated:
        return render(request, 'suggestions/suggestion.html', context)

    elif request.user.is_authenticated:
        form = SuggestionForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            suggestion = form.save(commit=False)
            suggestion.user = request.user
            suggestion.save()
            for f in request.POST.getlist('filter'):
                suggestion.filters.add(Filter.objects.get(pk=f))
            return redirect('home')
        else:
            context['form'] = form
            return render(request, 'suggestions/suggestion.html', context)
    else:
        return HttpResponseForbidden()
