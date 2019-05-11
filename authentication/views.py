import json

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_slug, validate_email
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.views.generic import View

from authentication.models import Profile
from .forms import LoginForm, RegisterForm
from django.core.mail import send_mail
from django.contrib.auth import logout


class LoginFormView(View):
    template_name = 'authentication/login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class(None)
        if not request.user.is_authenticated:
            return render(request, self.template_name, {'form': form})
        else:
            return redirect('home')

    def post(self, request):
        form = self.form_class(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not Profile.objects.filter(email=email).exists():
            form.add_error('email', 'Fant ingen bruker med den eposten')
        else:
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')

            form.add_error('password', 'Feil brukernavn eller passord')
        # Refreshes the login form if not correct
        return render(request, self.template_name, {'form': form})


def send_confiramtion_email(user_email):
    send_mail(
        "Velkommen til Leonardos nettside",  # Subject
        "Hei!\nVelkommen til Leonardos nettside. Her kan du melde deg på arrangementer, legge ut prosjektene dine på prosjektsiden og skrive artikler til wikisiden vår.\n\nMvh. Leonardo linjeforening",
        # Message
        settings.EMAIL_HOST_USER,  # From email
        [user_email],  # To email
        fail_silently=False,
    )


def logout_view(request):
    logout(request)
    return redirect('home')


def check_email(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print(request.POST)
        if not form.is_valid():
            return JsonResponse(form.errors)
        else:
            return HttpResponse(True)
    else:
        return HttpResponse('Error')


def register(request):
    # process form data
    if request.method == 'POST':
        # Cleaned (normalized) data
        form = RegisterForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save(commit=False)
            email = form.cleaned_data['email']
            firstname = form.cleaned_data['first_name']
            lastname = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            user = Profile.objects.create(email=email,
                                      first_name=firstname,
                                      last_name=lastname)

            user.set_password(password)
            user.save()
            # Returns User objects if credentials are correct
            user = authenticate(email=email, password=password)

            if user is not None:
                # send_confiramtion_email(user.email)
                if user.is_active:
                    login(request, user)  # Loging in user to the website
                    return HttpResponse(True)
            else:
                return HttpResponse(False)
        else:
            return HttpResponse(form.errors)




def PasswordResetView(request):
    template_name = 'authentication/password_reset_form.html'

    return render(request, template_name, {})
